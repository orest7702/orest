from flask import Flask, request, render_template
import pymysql

app = Flask(__name__)

# Параметри підключення до бази даних
def get_db_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='my_database'
    )

@app.route('/')
def index():
    return render_template('index.html')  # Ваша HTML-сторінка

@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form['name']
    email = request.form['email']

    # Підключення до бази даних
    connection = get_db_connection()
    cursor = connection.cursor()

    # Вставка даних у таблицю
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
