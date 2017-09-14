from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
import re, md5

app = Flask(__name__)
app.secret_key = "Shh..."
mysql = MySQLConnector(app, 'the_wall')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')



@app.route('/')
def home():
    return render_template('index.html')


@app.route('/wall')
def wall():
    # Showing who just logged in
    user_query = "select first_name from users where id = :id"
    user_data = {
        "id": session['logged_in_user']
    }
    first_name = mysql.query_db(user_query,user_data)

    #Showing the messages in the database
    messages_query = "select messages.id, users.first_name, users.last_name, messages.message, messages.created_at from users join messages on users.id = messages.user_id order by messages.created_at desc"
    messages = mysql.query_db(messages_query)

    #Showing comments in the database
    comment_query = "select users.id, messages.id, users.first_name, users.last_name, comments.comment, comments.created_at from comments join messages on comments.message_id = messages.id join users on users.id = comments.user_id order by comments.id"
    comments = mysql.query_db(comment_query)
    return render_template('the-wall.html', first_name = first_name, messages = messages, comments = comments)

@app.route('/log_off', methods=['POST'])
def log_off():
    return redirect('/')

@app.route('/post', methods=['POST'])
def post_message():
    # Adding message to database
    form_data = {
        "id" : session['logged_in_user'],
        'message' : request.form['message']
    }
    query = "insert into messages(user_id ,message, created_at, updated_at) values (:id ,:message, now(), now())"
    mysql.query_db(query,form_data)

    return redirect('/wall')

@app.route('/comment/<message_id>', methods=['POST'])
def comment(message_id):
    #Adding comment to database
    form_data = {
        "user_id" : session['logged_in_user'],
        "message_id" : message_id,
        "comment" : request.form['comment']
    }
    query = "insert into comments(comment, message_id, user_id, created_at, updated_at) values (:comment, :message_id, :user_id, now(), now())"
    mysql.query_db(query,form_data)

    return redirect('/wall')

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
        return redirect('/wall')
    
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
        return redirect('/wall')
    

app.run(debug=True)