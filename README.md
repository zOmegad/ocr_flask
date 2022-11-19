
# GrandpyBOT - OCR 🤖

Python3 flask app that find places and history about it, simply with Wikimedia and Mapbox API.

## Changelog
+mongodb database connection
+comment section with username, avatar
+sort system for reposted comments

## Requirement

python3 & pip

## Installation

```bash
$ pip install -r requirements.txt
```
To run server with debug mode :
```bash
$ FLASK_APP=app.py FLASK_ENV=development flask run
```

## Run tests
```bash
$ pytest
```

Coverage :
```bash
$ pytest --cov .
```  