import pytest
from mongoengine import connect
from app import *
import pymongo
from models.models import *

client = app.test_client()

def test_new_repost_is_recorded():
    my_db = connect(db="grandpy_bot_test", host="localhost", port=27017)
    new_repost = Repost(
                username = "Username",
                comment = "Cool comment",
                coordinate = [4, 4],
                city = "City",
                avatar = "https://ai-or-human.github.io/assets/emoji-ai.png",
                posted_at = datetime.now(),  
            )
    new_repost.save()
    new_post_id = new_repost.id
    my_db.close()
    post_request = client.post("/", data={'upvote': str(new_post_id), 'db_test': ''})
    assert post_request.status == '302 FOUND'

def test_new_upvote_is_added():
    my_db = connect(db="grandpy_bot_test", host="localhost", port=27017)
    upvoted_repost = Repost.objects.order_by('-id').first()
    my_db.close()
    assert upvoted_repost.upvote == 1

