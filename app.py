from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask import flash


db = SQLAlchemy()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'jvchujikhgtfdchujihnkogfcdj'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/colleg_orest'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


class Faculty(db.Model):
    __tablename__ = "specuality"

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
    status = db.Column(db.String(255))
    reside_code = db.Column(db.Integer)
    name_settlement = db.Column(db.String(255))
    math_grade = db.Column(db.Integer)
    uk_language = db.Column(db.Integer)
    specuality_id = db.Column(db.Integer, db.ForeignKey('specuality.id'), nullable=False)

    def __repr__(self):
        return f'Student ID: {self.id}'


@app.route('/')
def index():
    faculties = Faculty.query.all()
    return render_template("index.html", faculties=faculties)


@app.route('/new_faculty', methods=["POST", "GET"])
def new_faculty():
    if request.method == "POST":
        faculty_name = request.form["faculty_name"]
        faculty_code = request.form["faculty_code"]

        new_faculty = Faculty(faculty_name=faculty_name, faculty_code=faculty_code)
        db.session.add(new_faculty)
        db.session.commit()

        return redirect(url_for('index'))  # Повернення до головної сторінки або іншого списку факультетів

    return render_template('new_faculty.html')


@app.route('/new_student/<int:faculty_id>', methods=["POST", "GET"])
def new_student(faculty_id):
    faculty = Faculty.query.get_or_404(faculty_id)
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
        faculty_id = request.form["faculty_id"]

        new_student = Student(
            name=name,
            last_name=last_name,
            first_name=first_name,
            person_number=person_number,
            status=status,
            reside_code=reside_code,
            name_settlement=name_settlement,
            math_grade=math_grade,
            uk_language=uk_language,
            specuality_id=faculty_id)
        db.session.add(new_student)
        db.session.commit()

        return redirect(url_for('faculty_students', faculty_id=faculty_id))

    return render_template('new_student.html', faculty=faculty)


@app.route('/faculty/<int:faculty_id>')
def faculty_students(faculty_id):
    faculty = Faculty.query.get_or_404(faculty_id)
    students = Student.query.filter_by(specuality_id=faculty_id).all()
    return render_template("students_list.html", faculty=faculty, students=students)


@app.route('/new_table_student/<int:faculty_id>', methods=["POST", "GET"])
def new_table_student(faculty_id):
    faculty = Faculty.query.get_or_404(faculty_id)
    return render_template('new_table.html', faculty=faculty)



@app.route('/delete_student/<int:student_id>', methods=["POST", "GET"])
def delete_student(student_id):
    student = Student.query.get_or_404(student_id)
    if student:
        db.session.delete(student)
        db.session.commit()
    return redirect(url_for('index'))


@app.route('/delete_faculty/<int:id>', methods=["POST", "GET"])
def delete_faculty(id):
    faculty = Faculty.query.get_or_404(id)
    if faculty:
        db.session.delete(faculty)
        db.session.commit()
    return redirect(url_for('index'))


@app.route('/edit_faculty/<int:id>', methods=['GET', 'POST'])
def edit_faculty(id):
    faculty = Faculty.query.get_or_404(id)  # Отримуємо факультет або повертаємо 404

    if request.method == 'POST':
        faculty.faculty_name = request.form['faculty_name']
        faculty.faculty_code = request.form['faculty_code']

        db.session.commit()  # Зберігаємо зміни в базі даних
        flash('Дані факультету оновлено!', 'success')
        return redirect(url_for('index'))

    return render_template('new_faculty.html', faculty=faculty)


@app.route('/get_all_students', methods=["POST", "GET"])
def get_all_students():
    students = Student.query.all()
    return render_template('students_list.html', students=students)


@app.route('/edit_student/<int:student_id>', methods=['GET', 'POST'])
def edit_student(student_id):
    student = Student.query.get_or_404(student_id)  # Отримуємо студента або повертаємо 404

    if request.method == 'POST':
        student.name = request.form['name']
        student.last_name = request.form['last_name']
        student.first_name = request.form['first_name']
        student.person_number = request.form['person_number']
        student.status = request.form['status']
        student.reside_code = request.form['reside_code']
        student.name_settlement = request.form['name_settlement']
        student.math_grade = request.form['math_grade']
        student.uk_language = request.form['uk_language']
        student.specuality_id = request.form['specuality_id']

        db.session.commit()  # Зберігаємо зміни в базі даних
        flash('Дані студента оновлено!', 'success')
        return redirect(url_for('index'))

    return render_template('ful_student.html', student=student)

if __name__ == '__main__':
    app.run(debug=True)

