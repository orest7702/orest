from flask import Flask, request, jsonify
import pymysql
from syudent import syudent

app = Flask(__name__)

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='colleg_orest',
    cursorclass=pymysql.cursors.DictCursor
)