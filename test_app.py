from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, render_template, redirect, url_for
from model_student import Student, db
import pymysql


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/colleg_orest'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#db = SQLAlchemy(app)
db.init_app(app)

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='colleg_orest',
    cursorclass=pymysql.cursors.DictCursor
)
student_student = Student

#cursor.execute()
connection.commit()
@app.route('/')
def new_student():
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO student(name, last_name, first_name, person_number, status, reside_code, name_settlement, math_grade, uk_language) "
                       "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", ("Іван", "Бадьо", "Володимирович", "0935578432", "контракт", "243", "Київ", "10", "12"))
        connection.commit()  # Фіксація змін у базі даних

        tables = cursor.fetchall()
        print(tables)
        return redirect(url_for('index'))

def get_all_students():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM specuality")
        rr = cursor.fetchall()
        print(rr)
        return rr

def delet_student(id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM student WHERE id = %s", (id,))
        connection.commit()
        print(f"Студента з ID {id} успішно видалено.")
        connection.close()

new_student()

st = get_all_students()
print("Список факультетів:")
for student in st:
    print(student)

#delet_student(3)
'''
st = get_all_students()
print("Список студентів:")
for student in st:
    print(student)'''

if __name__ == '__main__':
    app.run(debug=True)