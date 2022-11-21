import pytest
from app import *

client = app.test_client()

def test_home_page_status():
    response = client.get("/")
    assert response.status == "200 OK"

def test_post_method_status():
    post_requete = client.post("/", data={'db_test': '', 'inputUsername': 'testing tests prout','inputAvatar': '', 'inputRepostText':'Testing repost text', 'inputData': 'City', 'inputCoordinates': '[120.930229378541, 23.7779779950014]'})
    assert post_requete.status == "302 FOUND"
