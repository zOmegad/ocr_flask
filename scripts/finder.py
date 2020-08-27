from flask import Flask, render_template, request, json
import requests
import string


class Finder():

    def __init__(self):
        self.resultat = None
        self.coo_x = None
        self.coo_y = None
        self.wiki_result = None
        self.wiki_search = None

    def cutter(self, awnser):
        with open('static/word.json', "r") as json_file:
            data = json.load(json_file)

            checker = [word for word in awnser.lower().split()
                       if word.lower() not in data]
            resultat = ' '.join(checker)
            # remove punctuation
            self.resultat = resultat.translate(str.maketrans(
                '', '', string.punctuation))

    def wiki_title(self):
        wiki_link = requests.get(
            "https://fr.wikipedia.org/w/api.php?action=query&list=search&srsearch="
            "{}&format=json".format(self.resultat))
        wiki_response = wiki_link.json()

        self.wiki_search = wiki_response["query"]["search"][0]["title"]
        self.wiki_result = wiki_response["query"]["search"][0]["snippet"]

    def wiki_text(self):
        wiki_text_link = requests.get("https://fr.wikipedia.org/w/api.php?"
                                      "action=query&prop=extracts&titles="
                                      "{}&format=json".format(self.wiki_search))
        wiki_text_response = wiki_text_link.json()

        wiki_page_id = wiki_text_response["query"]["pages"]
        for item in wiki_page_id:
            page_id = item
            break

        self.wiki_result = wiki_text_response["query"]["pages"][page_id]["extract"]

    def map_api(self):
        map_link = requests.get("https://api.mapbox.com/geocoding/v5/mapbox.places/{}.json?access_token=pk.eyJ1Ijoib21lZ2FkIiwiYSI6ImNrZGtlaTlsOTBvN2gydWxoYWQ4OWF4eHEifQ.oKS9ZV_VFYN4aQb294xTZw".format(self.wiki_search))
        map_response = map_link.json()
        coordinates = map_response["features"][0]["geometry"]["coordinates"]
        self.coo_y = coordinates[0]
        self.coo_x = coordinates[1]
