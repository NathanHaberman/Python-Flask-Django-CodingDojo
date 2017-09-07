from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def greeting():
    return render_template('index.html')

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')

@app.route('/dojo/new')
def dojo():
    return render_template('dojos.html')

@app.route('/dojo/new/post', methods=['POST'])
def form_post():
    print 'Got Post Info'
    name = request.form['name']
    email = request.form['email']
    return redirect('/dojo/new')

app.run(debug=True)