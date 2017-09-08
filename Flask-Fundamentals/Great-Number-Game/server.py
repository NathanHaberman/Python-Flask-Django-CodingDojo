from flask import Flask, render_template, request, redirect, session, flash
import random

app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/')
def home():
    if not session['the_number']:
        session['the_number'] = random.randrange(0,101)
    print session['the_number']
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    print type(session['the_number'])
    print type(session['guess'])
    if session['guess'] < session['the_number']:
        flash("Too low! Guess again!")
    elif session['guess'] > session['the_number']:
        flash("Too high! Guess again!")
    else:
        session['correct'] = True
        flash("You're Correct! The number is {}".format(session['the_number']))
        session['the_number'] = None
    return redirect('/')

@app.route('/reset')
def reset():
    session['correct'] = False
    return redirect('/')


app.run(debug=True)