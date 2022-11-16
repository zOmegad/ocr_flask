from flask import Flask, render_template, request, json, redirect
from scripts.finder import *
from models.models import *
import os
import ast
import pymongo
from bson.json_util import ObjectId
from mongoengine import connect
from datetime import datetime
from dotenv import load_dotenv
import string

app = Flask(__name__)
load_dotenv()


@app.route('/')
def home():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["grandpy_bot"]
    col = db["repost"]
    data = col.find({})
    map_api = os.getenv("MAP_API")
    return render_template('index.html', repost = data, map_key = map_api )


@app.route('/', methods=['POST'])
def sendRequest():
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
        return render_template('index.html', response=resultat, coordinate=coordonnes, wiki=my_finder.wiki_result[0:2000], map_key=map_api, data_wiki = wiki_search)

    if "inputRepost" in request.form:
        my_db = connect(db="grandpy_bot", host="localhost", port=27017)
        username_i = request.form["inputRepost"]
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
        except Exception as e:
            print(e)
        my_db.close()
        return redirect('/')

    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["grandpy_bot"]
    col = db["repost"]

    if "alphabetic" in request.form:
        print('--------------ALPHABETIC-----------')
        data_find = col.find({})
        data = data_find.sort('city', pymongo.ASCENDING)
        map_api = os.getenv("MAP_API")
        return render_template('index.html', repost = data, map_key = map_api )

    if "recent" in request.form:
        print('--------------RECENT-----------')
        data_find = col.find({})
        data = data_find.sort('posted_at', pymongo.DESCENDING)
        map_api = os.getenv("MAP_API")
        return render_template('index.html', repost = data, map_key = map_api )

    if "oldest" in request.form:
        data_find = col.find({})
        data = data_find.sort('posted_at', pymongo.ASCENDING)
        map_api = os.getenv("MAP_API")
        return render_template('index.html', repost = data, map_key = map_api )

    if "popular" in request.form:
        print('--------------POPULAR-----------')
        data_find = col.find({})
        data = data_find.sort('upvote', pymongo.DESCENDING)
        map_api = os.getenv("MAP_API")
        return render_template('index.html', repost = data, map_key = map_api )
    
    if "upvote" in request.form:
        # mongoengine
        my_db = connect(db="grandpy_bot", host="localhost", port=27017)
        post_id = request.form["upvote"]
        data = Repost.objects.get(id=post_id)
        current_upvote = data.upvote + 1
        data.update(upvote=current_upvote)
        my_db.close()

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
