from mongoengine import Document, ListField, StringField, URLField, DateTimeField, ListField

class Repost(Document):
    username = StringField(required=True, max_length=70)
    comment = StringField(required=True)
    coordinate = ListField(required=True)
    city = StringField(required=True, max_length=70)
    posted_at = DateTimeField(required=True)
