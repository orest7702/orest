from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, render_template
from model_student import Student
import pymysql


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/colleg_orest'
#db.session.add(Student)db.session.commit()
db = SQLAlchemy(app)

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='colleg_orest',
    cursorclass=pymysql.cursors.DictCursor
)


#cursor.execute()
connection.commit()
with connection.cursor() as cursor:
    cursor.execute("INSERT INTO student(name, last_name, first_name, person_namber, statys, reside_code, name_settlement, math_grade, uk_language) "
                   "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", ("Іван ", "бадь", "Іванович", "5654366655", "контракт", "38", "строннятин", "12", "4",))
    connection.commit()  # Фіксація змін у базі даних

    cursor.execute("SHOW DATABASES")
    tables = cursor.fetchall()
    print(tables)

connection.close()
cursor.close()