from sqlalchemy import create_engine, inspect, text
import sqlalchemy
import os
from dotenv import load_dotenv 
from flask import Flask, render_template, request

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Connection string
conn_string = (
    f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}")
engine = create_engine(conn_string)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/patients')
def patients():
    with engine.connect() as connection:
        query_1 = text('SELECT * FROM patients')
        result_1 = connection.execute(query_1)
        table_1 = result_1.fetchall()

    return render_template('patients.html', data1=table_1)

@app.route('/medication')
def medication():
    with engine.connect() as connection:
        query_2 = text('SELECT * FROM patient_medication')
        result_2 = connection.execute(query_2)
        table_2 = result_2.fetchall()

    return render_template('medication.html', data2=table_2)

if __name__ == '__main__':
    app.run(debug=True)
