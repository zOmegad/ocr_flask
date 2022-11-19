import pytest
import datetime
from models.models import *

def test_create_repost_orm():
    post = Repost(
        username = "Bob",
        comment = "Super cool",
        coordinate = [2.3483915, 48.8534951],
        city = "Paris",
        avatar = "avatar.jpg",
        posted_at = datetime.datetime(2022, 11, 17, 17, 42, 30, 517000),
    )
    
    assert post.username == "Bob"
    assert post.comment == "Super cool"
    assert post.coordinate == [2.3483915, 48.8534951]
    assert post.city == "Paris"
    assert post.avatar == "avatar.jpg"
    assert post.posted_at == datetime.datetime(2022, 11, 17, 17, 42, 30, 517000)