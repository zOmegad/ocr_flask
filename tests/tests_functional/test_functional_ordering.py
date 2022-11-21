import pytest
from app import *

client = app.test_client()

def test_alphabetic_page_content():
    pass
"""
    post_requete = client.post("/", data={'db_test': '', 'inputUsername': 'Username','inputAvatar': '', 'inputRepostText':'Testing repost text', 'inputData': 'AAA', 'inputCoordinates': '[120.930229378541, 23.7779779950014]'})
    db_client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = db_client["grandpy_bot"]
    col = db["repost"]
    requete_alpha = client.get('/alphabetic')
    assert "test" == requete_alpha.data
"""