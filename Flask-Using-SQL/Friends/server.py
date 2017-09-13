from flask import Flask, render_template, redirect, request
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app,'friends')

@app.route('/')
def home():
    query = "select * from friends"
    friends = mysql.query_db(query)
    return render_template('index.html', friends = friends)

@app.route('/add_friend', methods=['POST'])
def add_friend():
    query = "insert into friends(name, age, created_at, updated_at) values (:name, :age, now(),now())"
    data = {
        'name': request.form['name'],
        'age': request.form['age']
    }

    mysql.query_db(query,data)
    return redirect('/')

app.run(debug=True)