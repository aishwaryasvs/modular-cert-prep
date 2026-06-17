import os
import unittest
import json
from app import app, db, User, Certification, Question

class TestCertPrepAuthAndDB(unittest.TestCase):
    def setUp(self):
        # Configure app for testing
        app.config['TESTING'] = True
        # Use an in-memory SQLite database for test isolation
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['WTF_CSRF_ENABLED'] = False
        
        self.client = app.test_client()
        
        # Create all tables and seed within app context
        with app.app_context():
            db.create_all()
            # We can also verify that seeding works on an empty DB
            from app import seed_database_from_json
            seed_database_from_json()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_unauthenticated_redirect(self):
        # Accessing index should redirect to login
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login', response.headers['Location'])

        # Accessing certifications API should also redirect to login
        response = self.client.get('/api/certifications')
        self.assertEqual(response.status_code, 302)

    def test_registration_and_login_flow(self):
        # 1. Register a new user
        response = self.client.post('/register', data={
            'username': 'testuser',
            'password': 'testpassword'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        
        # Verify the user is created in database
        with app.app_context():
            user = User.query.filter_by(username='testuser').first()
            self.assertIsNotNone(user)
            self.assertTrue(user.check_password('testpassword'))
            
        # The redirection should take the registered user to the dashboard
        # Let's check that we can now fetch /api/certifications
        response = self.client.get('/api/certifications')
        self.assertEqual(response.status_code, 200)
        certs = json.loads(response.data)
        
        # We expect certifications to be loaded (e.g. google-cloud-digital-leader, google-generative-ai-leader, google-associate-cloud-engineer, etc.)
        self.assertGreater(len(certs), 0)
        cert_ids = [c['id'] for c in certs]
        self.assertIn('google-associate-cloud-engineer', cert_ids)
        self.assertIn('google-cloud-digital-leader', cert_ids)
        self.assertIn('google-generative-ai-leader', cert_ids)

        # 2. Log out
        response = self.client.get('/logout', follow_redirects=True)
        # Logout redirects to login page
        self.assertIn('Log in to your study workspace', response.data.decode('utf-8'))

        # Accessing / again should redirect
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)

        # 3. Log back in
        response = self.client.post('/login', data={
            'username': 'testuser',
            'password': 'testpassword'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        
        # Accessing API should work again
        response = self.client.get('/api/certifications')
        self.assertEqual(response.status_code, 200)

    def test_invalid_login(self):
        # Try logging in with non-existent user
        response = self.client.post('/login', data={
            'username': 'invaliduser',
            'password': 'somepassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Invalid username or password.', response.data.decode('utf-8'))

    def test_duplicate_registration(self):
        # Register user first time
        response = self.client.post('/register', data={
            'username': 'dupuser',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 302)

        # Use a new client to avoid active session redirect
        new_client = app.test_client()
        # Register same username again
        response = new_client.post('/register', data={
            'username': 'dupuser',
            'password': 'newpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Username is already taken.', response.data.decode('utf-8'))

if __name__ == '__main__':
    unittest.main()
