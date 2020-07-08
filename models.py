from flask_sqlalchemy import SQLAlchemy

from .views import app

# Create database connection object
db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(200), nullable=False)
    awnser = db.Column(db.Text(1200), nullable=False)

    def __init__(self, question, awnser):
        self.question = question
        self.awnser = awnser

db.create_all()