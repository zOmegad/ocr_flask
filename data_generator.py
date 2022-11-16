from mongoengine import connect
import pymongo
import random
from models.models import *
from datetime import datetime
from faker import Faker

fake = Faker()

my_db = connect(db="grandpy_bot", host="localhost", port=27017)
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["grandpy_bot"]
col = db["repost"]
data = col.find({})

col.drop()

for i in range(25):
    new_repost = Repost(
        username = fake.name(),
        comment = fake.text(max_nb_chars=30),
        coordinate = [-70.322226, 43.530977],
        city = fake.city(),
        avatar = "https://ai-or-human.github.io/assets/emoji-ai.png",
        posted_at = datetime.now(),
        upvote = random.randint(0,100),
    )
    print(i)
    new_repost.save()

my_db.close()
