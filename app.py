from flask import Flask, render_template, request, json

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def sendRequest():
    user =  request.form['username'];
    password = request.form['password'];
    return render_template('index.html', awnser=user)

if __name__=="__main__":
    app.run()
