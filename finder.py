from flask import Flask, render_template, request, json
import requests
import string


class Finder():

    def __init__(self):
        self.resultat = None
        self.coo_x = None
        self.coo_y = None
        self.wiki_result = None

    def cutter(self, awnser):
        with open('word.json', "r") as json_file:
            data = json.load(json_file)

            checker = [word for word in awnser.lower().split()
                       if word.lower() not in data]
            resultat = ' '.join(checker)
            # remove punctuation
            self.resultat = resultat.translate(str.maketrans(
                '', '', string.punctuation))

    def wiki(self):
        wiki_link = requests.get(
            "https://fr.wikipedia.org/w/api.php?action=query&list=search&srsearch="
            "{}&format=json".format(self.resultat))
        wiki_response = wiki_link.json()

        wiki_search = wiki_response["query"]["search"][0]["title"]
        self.wiki_result = wiki_response["query"]["search"][0]["snippet"]

        wiki_coo_link = requests.get("https://fr.wikipedia.org/w/api.php?"
                                     "action=query&prop=coordinates&titles="
                                     "{}&format=json".format(wiki_search))
        wiki_coo_response = wiki_coo_link.json()

        wiki_coo = wiki_coo_response["query"]["pages"]

        for item in wiki_coo:
            page_id = item
            break

        try:
            self.coo_x = wiki_coo[page_id]["coordinates"][0]["lat"]
            self.coo_y = wiki_coo[page_id]["coordinates"][0]["lon"]
        except Exception:
            pass

        wiki_text_link = requests.get("https://fr.wikipedia.org/w/api.php?"
                                      "action=query&prop=extracts&titles="
                                      "{}&format=json".format(wiki_search))
        wiki_text_response = wiki_text_link.json()

        self.wiki_result = wiki_text_response["query"]["pages"][page_id]["extract"]
