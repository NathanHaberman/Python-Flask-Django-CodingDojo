from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    location = request.form['locations']
    comments = request.form['comments']
    return render_template('submitted.html', name= name, location= location, comments= comments)

app.run(debug=True)
