import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_talisman import Talisman

# Define a Config class for configuration settings
class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', 'sqlite:///site.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

app = Flask(__name__)

# Initialize database
db = SQLAlchemy(app)

# Set configuration based on environment
if os.environ.get('FLASK_ENV') == 'production':
    app.config.from_object(ProductionConfig)
    Talisman(app)
else:
    app.config.from_object(DevelopmentConfig)



#app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#db = SQLAlchemy(app)

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

@app.route('/Lesson_From_Life')
def lesson_from_life():
    record_visit('lesson_from_life')
    return render_template('Lesson_From_Life.html')

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


# if __name__ == '__main__':
#    app.debug = False
#        db.create_all()
#    port = int(os.environ.get('PORT', 5000))
#    app.run(host='0.0.0.0', port=port)

if __name__ == '__main__':
    # Removed db.create_all() for production
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
