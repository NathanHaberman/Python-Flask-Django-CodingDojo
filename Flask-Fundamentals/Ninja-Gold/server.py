from flask import Flask, render_template, redirect, request, session, flash
import random


app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/')
def home():
    if not session.get('gold'):
        session['gold'] = 0
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    buildings = {"farm": random.randint(10,20),"cave": random.randint(5,10),"house": random.randint(2,5),"casino": random.randint(0,50)}
    selected = request.form['building']
    session.pop('activity', None)
    if not session.get('log'):
        session['log'] = []
    
    if selected == "casino":
        win_or_loss = random.randint(0,3)
        if win_or_loss >= 1:
            if session['gold'] >= buildings.get(selected):
                session['gold'] -= buildings.get(selected)
                session['activity'] = "You lost " + str(buildings.get(selected)) + " gold at the " + selected
            else:
                session['gold'] = 0
                session['activity'] = "You lost all your gold at the " + selected
        else:
            session['gold'] += buildings.get(selected)
            session['activity'] = "You won " + str(buildings.get(selected)) + " gold at the " + selected
    else:
        session['gold'] += buildings.get(selected)
        session['activity'] = "You earned " + str(buildings.get(selected)) + " gold from the " + selected
    
    session['log'].append(session['activity'])
    
    print session['log']
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)