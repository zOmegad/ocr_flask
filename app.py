from flask import Flask, render_template, request, json
from scripts.finder import *
import os
from dotenv import load_dotenv
import string

app = Flask(__name__)
load_dotenv()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def sendRequest():
    awnser = request.form['question']
    awnser = awnser.translate(str.maketrans(
        string.punctuation, ' '*len(string.punctuation)))
    my_finder = Finder()
    my_finder.cutter(awnser)
    my_finder.wiki_title()
    my_finder.wiki_text()
    my_finder.map_api()

    coordonnes = [my_finder.coo_y, my_finder.coo_x]
    map_api = os.getenv("MAP_API")
    resultat = my_finder.resultat
    return render_template('index.html', response=resultat, coordinate=coordonnes, wiki=my_finder.wiki_result[0:2000], map_key=map_api)


if __name__ == "__main__":
    app.run(debug=True)
