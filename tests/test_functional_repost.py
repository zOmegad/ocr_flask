import pytest
from app import *

client = app.test_client()

def test_home_page_status():
    response = client.get("/")
    assert response.status == "200 OK"

def test_post_method_status():
    post_requete = client.post("/datdsqdsqdddqda")
    assert post_requete.status == "200 OK"

def test_range_by_alphabetic_post_method_status():
    #post_request = client.post("/")
    pass