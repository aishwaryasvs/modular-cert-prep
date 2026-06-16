import os
import json
from flask import Flask, jsonify, render_template, abort

app = Flask(__name__)

# Helper to load data
def load_questions_data():
    data_path = os.path.join(app.root_path, 'data', 'questions.json')
    try:
        with open(data_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading questions data: {e}")
        return {"certifications": []}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/certifications', methods=['GET'])
def get_certifications():
    data = load_questions_data()
    summary = []
    for cert in data.get("certifications", []):
        summary.append({
            "id": cert.get("id"),
            "name": cert.get("name"),
            "description": cert.get("description"),
            "icon": cert.get("icon", "📄"),
            "questionCount": len(cert.get("questions", []))
        })
    return jsonify(summary)

@app.route('/api/certifications/<cert_id>', methods=['GET'])
def get_certification_details(cert_id):
    data = load_questions_data()
    for cert in data.get("certifications", []):
        if cert.get("id") == cert_id:
            return jsonify(cert)
    abort(404, description="Certification not found")

if __name__ == '__main__':
    # Run in debug mode on host 0.0.0.0 and port 8080 (avoids macOS port 5000 conflicts)
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=True)

