from flask import Flask, render_template, request, json
import requests

class Finder():

	def __init__(self):
		self.resultat = None
		self.coo_x = None
		self.coo_y = None
		self.wiki_result = None

	def cutter(self, awnser):
		with open('word.json', "r") as json_file:
			data = json.load(json_file)

			checker = [word for word in awnser.lower().split() if word.lower() not in data]
			self.resultat = ' '.join(checker)
			self.mapper()
			self.wiki()

	def mapper(self):
		map_link = requests.get('https://api.mapbox.com/geocoding/v5/mapbox.places/{}.json?access_token=pk.eyJ1Ijoib21lZ2FkIiwiYSI6ImNrZGtlaTlsOTBvN2gydWxoYWQ4OWF4eHEifQ.oKS9ZV_VFYN4aQb294xTZw'.format(self.resultat))
		map_response = map_link.json()

		self.coo_x = map_response["features"][0]["bbox"][0]
		self.coo_y = map_response["features"][0]["bbox"][1]

	def wiki(self):
		wiki_link = requests.get("https://fr.wikipedia.org/w/api.php?action=query&list=search&srsearch={}&format=json".format(self.resultat))
		wiki_response = wiki_link.json()

		wiki_search = wiki_response["query"]["search"][0]["title"]
		self.wiki_result = wiki_response["query"]["search"][0]["snippet"]

		wiki_coo_link = requests.get("https://fr.wikipedia.org/w/api.php?action=query&prop=coordinates&titles={}&format=json".format(wiki_search))
		wiki_coo_response = wiki_coo_link.json()

		wiki_coo = wiki_coo_response["query"]["pages"]

		for item in wiki_coo:
			page_id = item
			break

		self.coo_x = wiki_coo[page_id]["coordinates"][0]["lat"]
		self.coo_y = wiki_coo[page_id]["coordinates"][0]["lon"]

		wiki_text_link = requests.get("https://fr.wikipedia.org/w/api.php?action=query&prop=extracts&exchars=800&titles={}&format=json".format(wiki_search))
		wiki_text_response = wiki_text_link.json()

		self.wiki_result = wiki_text_response["query"]["pages"][page_id]["extract"]