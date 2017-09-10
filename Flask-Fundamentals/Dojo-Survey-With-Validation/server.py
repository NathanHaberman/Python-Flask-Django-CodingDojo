from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = "Shhhh..."

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    location = request.form['locations']
    comments = request.form['comments']
    messages = False
    if len(name) == 0:
        flash("Name cannot be empty")
        messages = True
    if len(comments) == 0:
        flash("Comments cannot be empty")
        messages = True
    if len(comments) >= 120:
        flash("Comments cannot be longer than 120 characters")
        messages = True
    if messages:
        return redirect('/')
    else:
        return render_template('submitted.html', name= name, location= location, comments= comments)

app.run(debug=True)
