from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/colleg_orest'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


class Faculty(db.Model):
    __tablename__ = "specuality"  # Виправлено на правильну назву таблиці

    id = db.Column(db.Integer, primary_key=True)
    faculty_name = db.Column(db.String(255), nullable=False)
    faculty_code = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'<Faculty {self.faculty_name} (ID: {self.id})>'


class Student(db.Model):
    __tablename__ = "student"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    person_number = db.Column(db.Integer)
    status = db.Column(db.String(255))  # Виправлено на правильну назву
    reside_code = db.Column(db.Integer)
    name_settlement = db.Column(db.String(255))
    math_grade = db.Column(db.Integer)
    uk_language = db.Column(db.Integer)  # Виправлено на правильну назву
    specuality_id = db.Column(db.Integer, db.ForeignKey('specuality.id'), nullable=False)  # Виправлено на правильну назву

    def __repr__(self):
        return 'Student ID: {}'.format(self.id)


@app.route('/new_student', methods=["POST", "GET"])
def new_student():
    if request.method == "POST":
        name = request.form["fname"]
        last_name = request.form["sname"]
        first_name = request.form["spname"]
        person_number = request.form["onname"]
        status = request.form["kbn"]
        reside_code = request.form["cvil"]
        name_settlement = request.form["vname"]
        math_grade = request.form["marmath"]
        uk_language = request.form["marukr"]

        new_student = Student(
            name=name,
            last_name=last_name,
            first_name=first_name,
            person_number=person_number,  # Виправлено
            status=status,  # Виправлено
            reside_code=reside_code,
            name_settlement=name_settlement,
            math_grade=math_grade,
            uk_language=uk_language)  # Виправлено
        db.session.add(new_student)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('new_student.html')


@app.route('/')
def index():
    faculties = Faculty.query.all()
    return render_template("index.html", faculties=faculties)


@app.route('/faculty/<int:faculty_id>')
def faculty_students(faculty_id):
    faculty = Faculty.query.get_or_404(faculty_id)
    students = Student.query.filter_by(specuality_id=faculty_id).all()  # Виправлено на правильну назву
    return render_template("students_list.html", faculty=faculty, students=students)


@app.route('/delete_student/<int:id>', methods=["POST", "GET"])
def delete_student(id):
    student = Student.query.get(id)
    if student:
        db.session.delete(student)
        db.session.commit()  # Фіксуємо зміни в базі даних
        print(f"Студента з ID {id} успішно видалено.")
    return redirect(url_for('index'))


@app.route('/get_all_students', methods=["POST", "GET"])
def get_all_students():
    students = Student.query.all()  # Отримуємо всіх студентів з бази даних
    return render_template('students_list.html', students=students)


if __name__ == '__main__':
    app.run(debug=True)
