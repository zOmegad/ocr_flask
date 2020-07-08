import os

SECRET_KEY = "f)c#iV(\t/lw#pG\\cT<Oeyz&^"

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')