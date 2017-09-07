from flask import Flask, render_template

app = Flask(__name__)

@app.route('/ninjas/<color>')
def color(color):
    if color == "blue":
        return render_template('index.html', image="leonardo.jpg")
    elif color == "orange":
        return render_template('index.html', image="raphael.jpg")
    elif color == "red":
        return render_template('index.html', image="michelangelo.jpg")
    elif color == "purple":
        return render_template('index.html', image="donatello.jpg")
    else:
        return render_template('index.html', image="notapril.jpg")

@app.route('/ninjas/')
def all_tutrles():
    return render_template('index.html', image="tmnt.png")

app.run(debug=True)