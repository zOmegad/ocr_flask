from scripts.finder import Finder
import pytest
import json
import requests
from app import *


def test_wiki_returns_good_fields(monkeypatch):
	wiki_response = {
	   "batchcomplete":"",
	   "query":{
	      "searchinfo":{
	         "totalhits":112293
	      },
	      "search":[
	         {
	            "ns":0,
	            "title":"Londres",
	            "pageid":4924,
	            "size":167237,
	            "wordcount":16887,
	            "snippet":"Pour les articles homonymes, voir <span class=\"searchmatch\">Londres</span> (homonymie). <span class=\"searchmatch\">Londres</span> [lɔ̃dʁ] Écouter (en anglais : London [ˈlʌndən] Écouter) est la capitale et la plus grande",
	            "timestamp":"2020-08-22T15:44:54Z"
	         }
	      ]
	   }
	}
	finder = Finder()
	finder.resultat = "Londres"

	class MockReturn:

			def json():
				results_string = json.dumps(wiki_response)
				results_bytes = results_string.encode()
				result_json = json.loads(results_bytes)
				return result_json

	def mock_get_response(*args, **kwargs):
		return MockReturn


	monkeypatch.setattr('requests.get', mock_get_response)
	finder.wiki_title()
	assert finder.wiki_search == "Londres"

def test_wiki_text_returns_good_fields(monkeypatch):

	wiki_text_response = {
	  "batchcomplete": "",
	  "query": {
	    "pages": {
	      "4924": {
	        "pageid": 4924,
	        "ns": 0,
	        "title": "Londres",
	        "extract": "Article text"
	      }
	    }
	  }
	}
	finder = Finder()
	finder.wiki_search = "Londres"

	class MockReturn:

			def json():
				results_string = json.dumps(wiki_text_response)
				results_bytes = results_string.encode()
				result_json = json.loads(results_bytes)
				return result_json

	def mock_get_response(*args, **kwargs):
		return MockReturn


	monkeypatch.setattr('requests.get', mock_get_response)
	finder.wiki_text()
	assert finder.wiki_result == "Article text"

def test_map_api_returns_coordinates(monkeypatch):
	map_response = {
   "type":"FeatureCollection",
   "query":[
      "londres"
   ],
   "features":[
      {
         "id":"poi.420906857582",
         "type":"Feature",
         "place_type":[
            "poi"
         ],
         "relevance":1,
         "properties":{
            "foursquare":"4d1bcf18763fb1f7a5978566",
            "wikidata":"Q4043155",
            "address":"Londres 38",
            "category":"historic site, historic"
         },
         "geometry":{
            "coordinates":[
               -70.64812649999999,
               -33.444244499999996
            ],
            "type":"Point"
         }
      }
   ]
}

	finder = Finder()
	finder.wiki_map_api = "Londres"

	class MockReturn:

			def json():
				results_string = json.dumps(map_response)
				results_bytes = results_string.encode()
				result_json = json.loads(results_bytes)
				return result_json

	def mock_get_response(*args, **kwargs):
		return MockReturn


	monkeypatch.setattr('requests.get', mock_get_response)
	finder.map_api()
	assert finder.coo_y == -70.64812649999999
	assert finder.coo_x == -33.444244499999996

def test_cutter_returns_word():
	finder = Finder()
	awnser = "Ou est Londres ?"
	finder.cutter(awnser)

	assert finder.resultat == "londres "

def test_finder_function():
	client = app.test_client()
	post_request = client.post("/", data={'question': 'Londres'})
	print(post_request.data)
	assert "Londres" in str(post_request.data)
	assert "New-york" not in str(post_request.data)
