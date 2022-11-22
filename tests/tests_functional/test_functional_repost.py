import pytest
from mongoengine import connect
from app import *

client = app.test_client()

def test_home_page_status():
    response = client.get("/")
    assert response.status == "200 OK"

def test_post_method_status():
    post_request = client.post("/", data={'inputRepost':'', 'db_test': '', 'inputUsername': 'testing tests prout','inputAvatar': '', 'inputRepostText':'Testing repost text', 'inputData': 'City', 'inputCoordinates': '[120.930229378541, 23.7779779950014]'})
    assert post_request.status == "302 FOUND"

def test_repost_recorded():
    db_client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = db_client["grandpy_bot_test"]
    col = db["repost"]
    data_find = col.find({})
    data = data_find.sort('posted_at', pymongo.DESCENDING)
    all_data = []
    for i in data:
        all_data.append(i)
    assert "City" == all_data[0]["city"]
