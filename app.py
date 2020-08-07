from flask import Flask, render_template, request, json
from finder import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def sendRequest():
    awnser = request.form['question'];
    my_finder = Finder()
    my_finder.cutter(awnser)

    resultat = my_finder.resultat
    return render_template('index.html', response=resultat)

if __name__== "__main__":
    app.run(debug=True)
