from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/')
def home():
    session['count'] += 1
    return render_template("index.html")

@app.route('/add_2', methods=['POST'])
def add_2():
    session['count'] += 1
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['count'] = 0
    return redirect('/')

app.run(debug=True)