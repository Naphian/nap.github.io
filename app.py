import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Visit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    page_name = db.Column(db.String(100), nullable=False)

def record_visit(page_name):
    new_visit = Visit(timestamp=datetime.utcnow(), page_name=page_name)
    db.session.add(new_visit)
    db.session.commit()

@app.route('/')
def home():
    record_visit('home')
    return render_template('index.html')

@app.route('/AI_web')
def ai_web():
    record_visit('ai_web')
    return render_template('AI_web.html')

@app.route('/History')
def history():
    record_visit('history')
    return render_template('History.html')

@app.route('/Education_History')
def education_history():
    record_visit('education_history')
    return render_template('Education_History.html')

@app.route('/Experience')
def experience():
    record_visit('experience')
    return render_template('Experience.html')

@app.route('/Lesson_from_life')
def lesson_from_life():
    record_visit('lesson_from_life')
    return render_template('Lesson_from_life.html')

@app.route('/Reward')
def reward():
    record_visit('reward')
    return render_template('Reward.html')

@app.route('/Closing_Thoughts')
def closing_thoughts():
    record_visit('closing_thoughts')
    return render_template('Closing_Thoughts.html')

@app.route('/The_Exit')
def the_exit():
    record_visit('the_exit')
    return render_template('The_Exit.html')

@app.route('/view_visits')
def view_visits():
    visits = Visit.query.all()
    return render_template('view_visits.html', visits=visits)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

