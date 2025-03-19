from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    person_number = db.Column(db.Integer)
    statys = db.Column(db.String(255))
    reside_code = db.Column(db.Integer)
    name_settlement = db.Column(db.String(255))
    math_grade = db.Column(db.Integer)
    uk_language = db.Column(db.Integer)

    def __repr__(self):
        return 'Student ID: {}'.format(self.id)

'''
    name last_name first_name person_number statys reside_code name_settlement math_grade uk_language
'''