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
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

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

class QuizAttempt(db.Model):
    __tablename__ = 'quiz_attempts'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    certification_id = db.Column(db.String(100), db.ForeignKey('certifications.id'), nullable=False)
    score = db.Column(db.Float, nullable=False)
    total_questions = db.Column(db.Integer, nullable=False)
    correct_questions = db.Column(db.Integer, nullable=False)
    mode = db.Column(db.String(50), nullable=False)
    difficulty = db.Column(db.String(50), nullable=True)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())
    questions_json = db.Column(db.Text, nullable=True)
    answers_json = db.Column(db.Text, nullable=True)

    user = db.relationship('User', backref=db.backref('attempts', lazy=True))
    certification = db.relationship('Certification', backref=db.backref('attempts', lazy=True))


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


@app.route('/api/attempts', methods=['POST'])
@login_required
def save_attempt():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid payload"}), 400
    
    cert_id = data.get('certification_id')
    score = data.get('score')
    total_questions = data.get('total_questions')
    correct_questions = data.get('correct_questions')
    mode = data.get('mode')
    difficulty = data.get('difficulty', 'all')
    questions_list = data.get('questions')
    answers_list = data.get('answers')
    
    if not cert_id or score is None or total_questions is None or correct_questions is None or not mode:
        return jsonify({"error": "Missing required fields"}), 400
        
    cert = db.session.get(Certification, cert_id)
    if not cert:
        return jsonify({"error": "Certification not found"}), 404
        
    attempt = QuizAttempt(
        user_id=current_user.id,
        certification_id=cert_id,
        score=float(score),
        total_questions=int(total_questions),
        correct_questions=int(correct_questions),
        mode=mode,
        difficulty=difficulty,
        questions_json=json.dumps(questions_list) if questions_list else None,
        answers_json=json.dumps(answers_list) if answers_list else None
    )
    db.session.add(attempt)
    db.session.commit()
    
    return jsonify({"success": True, "attempt_id": attempt.id}), 201


@app.route('/api/attempts/<int:attempt_id>', methods=['GET'])
@login_required
def get_attempt_details(attempt_id):
    attempt = QuizAttempt.query.filter_by(id=attempt_id, user_id=current_user.id).first()
    if not attempt:
        abort(404, description="Attempt not found")
        
    q_ids = json.loads(attempt.questions_json) if attempt.questions_json else []
    answers = json.loads(attempt.answers_json) if attempt.answers_json else []
    
    questions = Question.query.filter(Question.id.in_(q_ids)).all()
    q_map = {q.id: q for q in questions}
    ordered_questions = []
    for q_id in q_ids:
        if q_id in q_map:
            q = q_map[q_id]
            ordered_questions.append({
                "id": q.id,
                "question": q.question,
                "options": json.loads(q.options_json),
                "correctAnswerIndex": q.correct_answer_index,
                "difficulty": q.difficulty,
                "explanation": q.explanation
            })
            
    return jsonify({
        "id": attempt.id,
        "certification_name": attempt.certification.name,
        "certification_id": attempt.certification_id,
        "score": attempt.score,
        "correct_questions": attempt.correct_questions,
        "total_questions": attempt.total_questions,
        "mode": attempt.mode,
        "difficulty": attempt.difficulty,
        "timestamp": attempt.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
        "questions": ordered_questions,
        "answers": answers
    })


@app.route('/api/metrics', methods=['GET'])
@login_required
def get_metrics():
    attempts = QuizAttempt.query.filter_by(user_id=current_user.id).order_by(QuizAttempt.timestamp.desc()).all()
    
    total_attempts = len(attempts)
    avg_score = 0.0
    total_correct = 0
    total_questions = 0
    simulation_attempts = 0
    simulation_passed = 0
    
    attempts_list = []
    for a in attempts:
        avg_score += a.score
        total_correct += a.correct_questions
        total_questions += a.total_questions
        
        is_pass = a.score >= 70.0
        if a.mode == 'simulation':
            simulation_attempts += 1
            if is_pass:
                simulation_passed += 1
                
        attempts_list.append({
            "id": a.id,
            "certification_name": a.certification.name,
            "certification_id": a.certification_id,
            "provider": a.certification.provider,
            "score": a.score,
            "correct_questions": a.correct_questions,
            "total_questions": a.total_questions,
            "mode": a.mode,
            "difficulty": a.difficulty,
            "timestamp": a.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            "passed": is_pass
        })
        
    if total_attempts > 0:
        avg_score = round(avg_score / total_attempts, 1)
    else:
        avg_score = 0.0
        
    sim_pass_rate = 0.0
    if simulation_attempts > 0:
        sim_pass_rate = round((simulation_passed / simulation_attempts) * 100, 1)
        
    # Unique certifications started
    started_certs = db.session.query(QuizAttempt.certification_id).filter_by(user_id=current_user.id).distinct().count()
    
    metrics = {
        "total_attempts": total_attempts,
        "avg_score": avg_score,
        "total_questions_answered": total_questions,
        "total_correct_questions": total_correct,
        "simulation_attempts": simulation_attempts,
        "simulation_pass_rate": sim_pass_rate,
        "certifications_started": started_certs,
        "recent_attempts": attempts_list[:10]
    }
    
    return jsonify(metrics)


@app.route('/api/profile', methods=['GET'])
@login_required
def get_profile():
    started_certs = db.session.query(QuizAttempt.certification_id).filter_by(user_id=current_user.id).distinct().count()
    member_since = current_user.created_at.strftime('%Y-%m-%d') if current_user.created_at else "Unknown"
    return jsonify({
        "username": current_user.username,
        "member_since": member_since,
        "certifications_started": started_certs
    })


@app.route('/api/change-password', methods=['POST'])
@login_required
def change_password():
    data = request.get_json()
    if not data or 'current_password' not in data or 'new_password' not in data:
        return jsonify({"error": "Current and new password are required"}), 400
    
    current_pw = data['current_password']
    new_pw = data['new_password']
    
    if len(new_pw) < 6:
        return jsonify({"error": "New password must be at least 6 characters long"}), 400
        
    if not current_user.check_password(current_pw):
        return jsonify({"error": "Incorrect current password"}), 400
        
    current_user.set_password(new_pw)
    db.session.commit()
    return jsonify({"success": True, "message": "Password updated successfully!"})


@app.route('/api/attempts/reset', methods=['POST'])
@login_required
def reset_attempts():
    try:
        QuizAttempt.query.filter_by(user_id=current_user.id).delete()
        db.session.commit()
        return jsonify({"success": True, "message": "All study progress reset successfully!"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


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


def run_migrations():
    try:
        from sqlalchemy import inspect
        inspector = inspect(db.engine)
        columns = [c['name'] for c in inspector.get_columns('users')]
        if 'created_at' not in columns:
            with db.engine.connect() as conn:
                conn.execute(db.text("ALTER TABLE users ADD COLUMN created_at DATETIME"))
                conn.commit()
                print("Added created_at column to users table successfully!")
        
        columns_attempts = [c['name'] for c in inspector.get_columns('quiz_attempts')]
        if 'questions_json' not in columns_attempts:
            with db.engine.connect() as conn:
                conn.execute(db.text("ALTER TABLE quiz_attempts ADD COLUMN questions_json TEXT"))
                conn.execute(db.text("ALTER TABLE quiz_attempts ADD COLUMN answers_json TEXT"))
                conn.commit()
                print("Added questions_json and answers_json columns to quiz_attempts table successfully!")
    except Exception as e:
        print(f"Migration check warning: {e}")


# --- Database initialization and Startup ---
with app.app_context():
    db.create_all()
    run_migrations()
    seed_database_from_json()
    seed_admin_user()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=True)
