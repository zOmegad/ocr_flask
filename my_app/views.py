from flask import Flask, render_template, request
from forms import PostForm

app = Flask(__name__)

app.config.from_object('config')
app.config['SECRET_KEY'] = "f)c#iV(\t/lw#pG\\cT<Oeyz&^"

@app.route('/', methods=['GET', 'POST'])

def index():
    form = PostForm()
    if form.is_submitted():
        result = request.form
        return render_template('index.html', form=form, result=result)
    return render_template('index.html', form=form)
