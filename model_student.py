from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    person_namber = db.Column(db.Integer)
    statys = db.Column(db.String(255))
    reside_code = db.Column(db.Integer)
    name_settlement = db.Column(db.String(255))
    math_grade = db.Column(db.Integer)
    uk_landuage = db.Column(db.Integer)

    def __repr__(self):
        return 'Student ID: {}'.format(self.id)
