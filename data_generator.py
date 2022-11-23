import random
from datetime import datetime
import pymongo
from mongoengine import connect
from mongoengine.connection import disconnect
from faker import Faker
from models.models import Repost

class DataGenerator():
    def __init__(self):
        self.db_name = "grandpy_bot"
        self.result = False

    def generate_data(self):
        fake = Faker()

        # Drop db
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client[self.db_name]
        col = db["repost"]
        col.drop()
        client.close()
        print(client.status)

        my_db = connect(db=self.db_name, host="localhost", port=27017)

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

        my_db = disconnect()
        self.result = True
        return self.result

if __name__ == "__main__":
    data_gen = DataGenerator()
    data_gen.generate_data()
