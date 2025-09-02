from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(200))
    role = db.Column(db.String(20))  # 'student' or 'faculty'

class Achievement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(200))
    category = db.Column(db.String(100))  # seminar, internship, etc.
    description = db.Column(db.Text)
    status = db.Column(db.String(20))  # pending, approved, rejected
