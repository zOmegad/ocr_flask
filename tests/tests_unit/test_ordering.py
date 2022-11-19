import pytest
from app import *

client = app.test_client()

def test_alphabetic_page_status():
    response = client.get("/alphabetic")
    assert response.status == "200 OK"

def test_recent_page_status():
    response = client.get("/recent")
    assert response.status == "200 OK"

def test_oldest_page_status():
    response = client.get("/oldest")
    assert response.status == "200 OK"

def test_popular_page_status():
    response = client.get("/popular")
    assert response.status == "200 OK"
