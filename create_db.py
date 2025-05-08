from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import db, app


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)  # ✅ Required
    password = db.Column(db.String(200), nullable=False)
    reset_token = db.Column(db.String(200))
    token_expiry = db.Column(db.DateTime)

# Ensure the database runs inside an app context
with app.app_context():
    db.create_all()
    print("Database tables created successfully!")
