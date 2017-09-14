from flask import Flask, render_template, redirect, request, flash
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
mysql = MySQLConnector(app,'emails')
app.secret_key = "Shhh...."
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/success')
def success():
    query = "select email, created_at from emails"
    emails = mysql.query_db(query)
    return render_template('success.html', emails = emails)

@app.route('/submit', methods=['POST'])
def submit():
    data = {
        'email' : request.form['email']
    }
    query = "select email from emails where email = :email"

    if not EMAIL_REGEX.match(data['email']):
        flash("Please enter a valid email")
        return redirect('/')
    elif mysql.query_db(query,data):
        flash("Email already taken")
        return redirect('/')
    else:
        flash(request.form['email'] + " was a valid email! Thank you!" )
        query = "insert into emails(email, created_at, updated_at) values (:email, now(), now())"
        data = {
            "email": request.form["email"]
        }
        mysql.query_db(query,data)
        return redirect('/success')


app.run(debug=True)