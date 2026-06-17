import os
import json
import string
import random
from flask import Flask, jsonify, render_template, abort, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default-dev-secret-key-12984712')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///certprep.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# --- SQLAlchemy Models ---

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    def set_password(self, password):
        from werkzeug.security import generate_password_hash
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.password_hash, password)

class Certification(db.Model):
    __tablename__ = 'certifications'
    id = db.Column(db.String(100), primary_key=True)
    provider = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    icon = db.Column(db.String(50), nullable=True)

    links = db.relationship('Link', backref='certification', cascade='all, delete-orphan')
    cheatsheet = db.relationship('Cheatsheet', backref='certification', uselist=False, cascade='all, delete-orphan')
    flashcards = db.relationship('Flashcard', backref='certification', cascade='all, delete-orphan')
    study_flashcards = db.relationship('StudyFlashcard', backref='certification', cascade='all, delete-orphan')
    questions = db.relationship('Question', backref='certification', cascade='all, delete-orphan')

class Link(db.Model):
    __tablename__ = 'links'
    id = db.Column(db.Integer, primary_key=True)
    certification_id = db.Column(db.String(100), db.ForeignKey('certifications.id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    url = db.Column(db.Text, nullable=False)

class Cheatsheet(db.Model):
    __tablename__ = 'cheatsheets'
    id = db.Column(db.Integer, primary_key=True)
    certification_id = db.Column(db.String(100), db.ForeignKey('certifications.id'), unique=True, nullable=False)
    summary = db.Column(db.Text, nullable=True)

    core_concepts = db.relationship('CoreConcept', backref='cheatsheet', cascade='all, delete-orphan')
    commands = db.relationship('Command', backref='cheatsheet', cascade='all, delete-orphan')
    patterns = db.relationship('ArchitecturalPattern', backref='cheatsheet', cascade='all, delete-orphan')

class CoreConcept(db.Model):
    __tablename__ = 'core_concepts'
    id = db.Column(db.Integer, primary_key=True)
    cheatsheet_id = db.Column(db.Integer, db.ForeignKey('cheatsheets.id'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    desc = db.Column(db.Text, nullable=False)

class Command(db.Model):
    __tablename__ = 'commands'
    id = db.Column(db.Integer, primary_key=True)
    cheatsheet_id = db.Column(db.Integer, db.ForeignKey('cheatsheets.id'), nullable=False)
    cmd = db.Column(db.Text, nullable=False)
    desc = db.Column(db.Text, nullable=False)

class ArchitecturalPattern(db.Model):
    __tablename__ = 'architectural_patterns'
    id = db.Column(db.Integer, primary_key=True)
    cheatsheet_id = db.Column(db.Integer, db.ForeignKey('cheatsheets.id'), nullable=False)
    scenario = db.Column(db.Text, nullable=False)
    solution = db.Column(db.Text, nullable=False)

class Flashcard(db.Model):
    __tablename__ = 'flashcards'
    id = db.Column(db.Integer, primary_key=True)
    certification_id = db.Column(db.String(100), db.ForeignKey('certifications.id'), nullable=False)
    category = db.Column(db.String(255), nullable=True)
    front = db.Column(db.Text, nullable=False)
    back = db.Column(db.Text, nullable=False)

class StudyFlashcard(db.Model):
    __tablename__ = 'study_flashcards'
    id = db.Column(db.Integer, primary_key=True)
    certification_id = db.Column(db.String(100), db.ForeignKey('certifications.id'), nullable=False)
    category = db.Column(db.String(255), nullable=True)
    front = db.Column(db.Text, nullable=False)
    back = db.Column(db.Text, nullable=False)

class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.String(150), primary_key=True)
    certification_id = db.Column(db.String(100), db.ForeignKey('certifications.id'), nullable=False)
    question = db.Column(db.Text, nullable=False)
    options_json = db.Column(db.Text, nullable=False)
    correct_answer_index = db.Column(db.Integer, nullable=False)
    difficulty = db.Column(db.String(50), nullable=False)
    explanation = db.Column(db.Text, nullable=False)


# --- User Loader ---
@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))


# --- Database Seeding Helper ---
def seed_database_from_json():
    # Only seed if no Certifications exist
    if Certification.query.first():
        return

    data_path = os.path.join(app.root_path, 'data', 'questions.json')
    if not os.path.exists(data_path):
        print("questions.json not found for seeding database!")
        return

    try:
        with open(data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        for cert_data in data.get("certifications", []):
            cert = Certification(
                id=cert_data["id"],
                provider=cert_data["provider"],
                name=cert_data["name"],
                description=cert_data.get("description"),
                icon=cert_data.get("icon")
            )
            db.session.add(cert)

            for link_data in cert_data.get("links", []):
                link = Link(
                    certification_id=cert.id,
                    title=link_data["title"],
                    url=link_data["url"]
                )
                db.session.add(link)

            cs_data = cert_data.get("cheatsheet")
            if cs_data:
                cs = Cheatsheet(
                    certification_id=cert.id,
                    summary=cs_data.get("summary")
                )
                db.session.add(cs)
                db.session.flush()

                for cc_data in cs_data.get("coreConcepts", []):
                    cc = CoreConcept(
                        cheatsheet_id=cs.id,
                        name=cc_data["name"],
                        desc=cc_data["desc"]
                    )
                    db.session.add(cc)

                for cmd_data in cs_data.get("commands", []):
                    cmd = Command(
                        cheatsheet_id=cs.id,
                        cmd=cmd_data["cmd"],
                        desc=cmd_data["desc"]
                    )
                    db.session.add(cmd)

                for pattern_data in cs_data.get("architecturalPatterns", []):
                    pat = ArchitecturalPattern(
                        cheatsheet_id=cs.id,
                        scenario=pattern_data["scenario"],
                        solution=pattern_data["solution"]
                    )
                    db.session.add(pat)

            for fc_data in cert_data.get("flashcards", []):
                fc = Flashcard(
                    certification_id=cert.id,
                    category=fc_data.get("category"),
                    front=fc_data["front"],
                    back=fc_data["back"]
                )
                db.session.add(fc)

            for sfc_data in cert_data.get("study_flashcards", []):
                sfc = StudyFlashcard(
                    certification_id=cert.id,
                    category=sfc_data.get("category"),
                    front=sfc_data["front"],
                    back=sfc_data["back"]
                )
                db.session.add(sfc)

            for q_data in cert_data.get("questions", []):
                q = Question(
                    id=q_data["id"],
                    certification_id=cert.id,
                    question=q_data["question"],
                    options_json=json.dumps(q_data["options"]),
                    correct_answer_index=q_data["correctAnswerIndex"],
                    difficulty=q_data["difficulty"],
                    explanation=q_data["explanation"]
                )
                db.session.add(q)

        db.session.commit()
        print("Database successfully seeded from questions.json!")
    except Exception as e:
        db.session.rollback()
        print(f"Error seeding database: {e}")


# --- Authentication Routes ---

def get_or_create_test_credentials():
    credentials_path = os.path.join(app.instance_path, 'test_credentials.json')
    os.makedirs(app.instance_path, exist_ok=True)
    if os.path.exists(credentials_path):
        try:
            with open(credentials_path, 'r') as f:
                return json.load(f)
        except Exception:
            pass
    chars = string.ascii_letters + string.digits
    username = 'test_admin_' + ''.join(random.choices(chars, k=6))
    password = ''.join(random.choices(chars, k=16))
    creds = {'username': username, 'password': password}
    try:
        with open(credentials_path, 'w') as f:
            json.dump(creds, f)
        print(f"Generated test credentials at {credentials_path}")
    except Exception as e:
        print(f"Error saving test credentials: {e}")
    return creds

@app.route('/login/bypass')
def login_bypass():
    creds = get_or_create_test_credentials()
    username = creds['username']
    password = creds['password']
    admin = User.query.filter_by(username=username).first()
    if not admin:
        admin = User(username=username)
        admin.set_password(password)
        db.session.add(admin)
        db.session.commit()
    login_user(admin)
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    error = None
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')
        
        if not username or not password:
            error = "Both username and password are required."
        elif User.query.filter_by(username=username).first():
            error = "Username is already taken."
        else:
            new_user = User(username=username)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('index'))
            
    return render_template('register.html', error=error)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
        
    error = None
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')
        
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('index'))
        else:
            error = "Invalid username or password."
            
    return render_template('login.html', error=error)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


# --- Public/API Endpoints (Adapted for relational DB) ---

@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/api/certifications', methods=['GET'])
@login_required
def get_certifications():
    summary = []
    certs = Certification.query.all()
    for cert in certs:
        q_count = Question.query.filter_by(certification_id=cert.id).count()
        sfc_count = StudyFlashcard.query.filter_by(certification_id=cert.id).count()
        links_data = [{"title": link.title, "url": link.url} for link in cert.links]

        summary.append({
            "id": cert.id,
            "name": cert.name,
            "description": cert.description,
            "icon": cert.icon or "📄",
            "provider": cert.provider,
            "links": links_data,
            "questionCount": q_count,
            "studyFlashcardCount": sfc_count
        })
    return jsonify(summary)

@app.route('/api/certifications/<cert_id>', methods=['GET'])
@login_required
def get_certification_details(cert_id):
    cert = db.session.get(Certification, cert_id)
    if not cert:
        abort(404, description="Certification not found")
    
    links_data = [{"title": link.title, "url": link.url} for link in cert.links]

    cs_data = None
    if cert.cheatsheet:
        cs_data = {
            "summary": cert.cheatsheet.summary,
            "coreConcepts": [{"name": cc.name, "desc": cc.desc} for cc in cert.cheatsheet.core_concepts],
            "commands": [{"cmd": c.cmd, "desc": c.desc} for c in cert.cheatsheet.commands],
            "architecturalPatterns": [{"scenario": p.scenario, "solution": p.solution} for p in cert.cheatsheet.patterns]
        }

    flashcards_data = [{
        "category": fc.category,
        "front": fc.front,
        "back": fc.back
    } for fc in cert.flashcards]

    study_flashcards_data = [{
        "category": sfc.category,
        "front": sfc.front,
        "back": sfc.back
    } for sfc in cert.study_flashcards]

    questions_data = [{
        "id": q.id,
        "question": q.question,
        "options": json.loads(q.options_json),
        "correctAnswerIndex": q.correct_answer_index,
        "difficulty": q.difficulty,
        "explanation": q.explanation
    } for q in cert.questions]

    result = {
        "id": cert.id,
        "provider": cert.provider,
        "name": cert.name,
        "description": cert.description,
        "icon": cert.icon,
        "links": links_data,
        "cheatsheet": cs_data,
        "flashcards": flashcards_data,
        "study_flashcards": study_flashcards_data,
        "questions": questions_data
    }
    return jsonify(result)


def seed_admin_user():
    creds = get_or_create_test_credentials()
    username = creds['username']
    password = creds['password']
    admin = User.query.filter_by(username=username).first()
    if not admin:
        admin = User(username=username)
        admin.set_password(password)
        db.session.add(admin)
        db.session.commit()
        print(f"Admin user {username} seeded successfully!")

# --- Database initialization and Startup ---
with app.app_context():
    db.create_all()
    seed_database_from_json()
    seed_admin_user()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=True)
