from flask import Flask, render_template, request, json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def sendRequest():
    awnser = request.form['question'];
    findPlace(awnser)
    return render_template('index.html', response=resultat)

def findPlace(awnser):
	print(awnser)

	with open('word.json', "r") as json_file:
		data = json.load(json_file)

		checker = [word for word in awnser.split() if word.lower() not in data]
		resultat = ' '.join(checker)
		print(resultat)


if __name__== "__main__":
    app.run(debug=True)
