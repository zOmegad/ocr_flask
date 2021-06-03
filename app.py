from flask import Flask, render_template, request, json, redirect
from scripts.finder import *
from models.models import *
import os
import ast
from mongoengine import connect
from datetime import datetime
from dotenv import load_dotenv
import string

app = Flask(__name__)
load_dotenv()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def sendRequest():
    if "question" in request.form:
        print("ceci est une recherche")
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
        wiki_search = my_finder.wiki_search
        return render_template('index.html', response=resultat, coordinate=coordonnes, wiki=my_finder.wiki_result[0:2000], map_key=map_api, data_wiki = wiki_search)

    if "inputRepost" in request.form:

        username = request.form["inputRepost"]
        message = request.form["inputRepostText"]
        data = request.form["inputData"]
        date_now = datetime.now()
        coordinates = ast.literal_eval(request.form["inputCoordinates"])
        print(date_now.strftime("%d/%m/%Y %H:%M:%S"))
        return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
