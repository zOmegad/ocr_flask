import os
import ast
import string
from datetime import datetime
from flask import Flask, render_template, request, redirect
import pymongo
from bson.json_util import ObjectId
from mongoengine import connect
from dotenv import load_dotenv
from scripts.finder import Finder
from models.models import Repost


app = Flask(__name__)
load_dotenv()
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["grandpy_bot"]
col = db["repost"]

@app.route('/')
def home():
    data = col.find({})
    map_api = os.getenv("MAP_API")
    return render_template('index.html', repost = data, map_key = map_api )

@app.route('/', methods=['POST'])
def send_request():
    if "question" in request.form:
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
        return render_template('index.html', response=resultat,
            coordinate=coordonnes,
            wiki=my_finder.wiki_result[0:2000],
            map_key=map_api,
            data_wiki = wiki_search)

    if "inputRepostText" in request.form:
        if 'db_test' in request.form:
            my_db = connect(db="grandpy_bot_test", host="localhost", port=27017)
        else:
            my_db = connect(db="grandpy_bot", host="localhost", port=27017)
        username_i = request.form["inputUsername"]
        message_i = request.form["inputRepostText"]
        city_i = request.form["inputData"]
        if not request.form["inputAvatar"]:
            avatar_i = "https://ai-or-human.github.io/assets/emoji-ai.png"
        else:
            avatar_i = request.form["inputAvatar"]
        coordinates_i = ast.literal_eval(request.form["inputCoordinates"])
        try:
            new_repost = Repost(
                username = username_i,
                comment = message_i,
                coordinate = coordinates_i,
                city = city_i,
                avatar = avatar_i,
                posted_at = datetime.now(),
            )
            new_repost.save()
        except Exception as error:
            print(error)
        my_db.close()

    if "upvote" in request.form:
        # mongoengine
        if 'db_test' in request.form:
            my_db = connect(db="grandpy_bot_test", host="localhost", port=27017)
        else:
            my_db = connect(db="grandpy_bot", host="localhost", port=27017)
        post_id = request.form["upvote"]
        data = Repost.objects.get(id=post_id)
        current_upvote = data.upvote + 1
        data.update(upvote=current_upvote)
        my_db.close()

    return redirect('/') # returns 302 code

@app.route('/alphabetic', methods=['GET'])
def alphabetic_sort():
    data_find = col.find({})
    data = data_find.sort('city', pymongo.ASCENDING)
    return render_template('index.html', repost = data)

@app.route('/recent', methods=['GET'])
def recent_sort():
    data_find = col.find({})
    data = data_find.sort('posted_at', pymongo.DESCENDING)
    return render_template('index.html', repost = data)

@app.route('/oldest', methods=['GET'])
def oldest_sort():
    data_find = col.find({})
    data = data_find.sort('posted_at', pymongo.ASCENDING)
    return render_template('index.html', repost = data)

@app.route('/popular', methods=['GET'])
def popular_sort():
    data_find = col.find({})
    data = data_find.sort('upvote', pymongo.DESCENDING)
    return render_template('index.html', repost = data)

if __name__ == "__main__":
    app.run(debug=True)
