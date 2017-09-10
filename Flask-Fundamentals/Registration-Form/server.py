from flask import Flask, render_template, request, redirect, session, flash
import re

app = Flask(__name__)
app.secret_key = "Shhhh..."
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=["POST"])
def submit():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    email = request.form["email"]
    password = request.form["password"]
    confirm_password = request.form["confirm_password"]
    messages = False
    # print first_name
    # print last_name
    # print email
    # print password
    # print confirm_password
    if len(first_name) == 0:
        flash("First name cannot be empty")
        massages = True
    if len(last_name) == 0:
        flash("Last name cannot be empty")
        messages = True
    if not EMAIL_REGEX.match(email):
        flash("Not a vaild email")
        messages = True
    if len(password) == 0 or len(confirm_password) == 0:
        flash("Please enter your password")
        messages = True
    if password != confirm_password:
        flash("Passwords do not match")
        messages = True
    if messages == False:
        flash("Form submit was successful!")
    return redirect('/')

app.run(debug=True)