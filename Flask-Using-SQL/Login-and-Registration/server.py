from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
import re, md5

app = Flask(__name__)
app.secret_key = "Shh..."
mysql = MySQLConnector(app, 'login_and_registration')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/success')
def success():
    # Showing who just logged in
    query = "select first_name from users where id = :id"
    data = {
        "id": session['logged_in_user']
    }
    first_name = mysql.query_db(query,data)

    return render_template('success.html', first_name = first_name)

@app.route('/login', methods=['POST'])
def login():
    # Gathering Form Data from index.html
    form_data = {
        'email' : request.form['login_email'],
        'password' : md5.new(request.form['login_password']).hexdigest()
    }

    # Checking the entered data to existing data in database
    query = "select id, email, password from users where email = :email and password = :password"
    login_check = mysql.query_db(query,form_data)

    # If it exists then log them in
    if login_check:
        session['logged_in_user'] = login_check[0]['id']
        return redirect('/success')
    
    # If it doesnt exist then flash message that it is incorrect
    else:
        flash("Email or password was incorrect")
        return redirect('/')


@app.route('/register', methods=['POST'])
def register():
    # Gathering Form Data from index.html
    form_data = {
        'first_name' : request.form['register_first_name'],
        'last_name' : request.form['register_last_name'],
        'email' : request.form['register_email'],
        'password' : request.form['register_password'],
        'confirm' : request.form['register_confirm_password']
    }

    # Used for email check
    query = "select email from users where email = :email"

    fail = False

    # Testing the names
    if len(form_data['first_name']) < 2 or len(form_data['last_name']) < 2:
        flash("First and last names must be at least 2 characters long")
        fail = True

    # Testing if vaild email
    if not EMAIL_REGEX.match(form_data['email']):
        flash("Enter a vaild email")
        fail = True

    # Checking is email is taken
    elif mysql.query_db(query,form_data):
        flash("Email is already taken")
        fail = True

    # Testing if passwords match
    if not form_data['password'] == form_data['confirm']:
        flash("Passwords do not match")
        fail = True

    # Testing to see if password is at least 8 characters
    if len(form_data['password']) < 8:
        flash("Password must be at least 8 characters")
        fail = True

    # If any fail go back to home
    if fail:
        return redirect('/')

    # If everything checks out!
    else:
        # Hashing password here
        hashed_password = md5.new(form_data['password']).hexdigest()
        form_data['password'] = hashed_password

        # Added data to my database
        query = "insert into users(first_name, last_name, email, password, created_at, updated_at) values (:first_name, :last_name, :email, :password, now(), now())"
        mysql.query_db(query,form_data)

        # Logging in the user who just registered
        query = "select id from users where email = :email"
        ids = mysql.query_db(query,form_data)
        session['logged_in_user'] = ids[0]['id']
        print session['logged_in_user']
        return redirect('/success')
    

app.run(debug=True)