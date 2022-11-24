
# GrandpyBOT - OCR 🤖

Python3 flask app that find places and history about it, simply with Wikimedia and Mapbox API.

## Improvements
#### 🌱 mongodb database connection
#### 💬 comment section with username, avatar
#### 🗃 sort system for reposted comments
 ⬆️ repost upvote system

## Requirement

- python3 & pip
- [Mongodb](https://www.mongodb.com/docs/manual/installation/)

## Installation

```bash
$ pip install -r requirements.txt
```
To run server with debug mode :
```bash
$ FLASK_APP=app.py FLASK_ENV=development flask run
```

##Generate data
```bash
$ python3 data_generator.py
```
## Run tests
```bash
$ pytest -vv
```

Coverage :
```bash
$ pytest --cov .
```  
