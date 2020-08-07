from flask import Flask, render_template, request, json

class Finder():

	def __init__(self):
		self.resultat = None

	def cutter(self, awnser):
		with open('word.json', "r") as json_file:
			data = json.load(json_file)

			checker = [word for word in awnser.split() if word.lower() not in data]
			self.resultat = ' '.join(checker)
			print(self.resultat)