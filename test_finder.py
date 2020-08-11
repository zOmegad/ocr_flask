import finder as script
import pytest

def test_resultat():
	finder = script.Finder()
	finder.resultat = "A result test string"
	assert finder.resultat == "A result test string"

def test_coordinate_float():
	finder = script.Finder()
	finder.coo_x = 3.1253114
	assert isinstance(finder.coo_x, float)
	finder.coo_y = 3.1253114
	assert isinstance(finder.coo_y, float)

def test_wiki_result():
	finder = script.Finder()
	finder.wiki_result = "A result test string"
	assert isinstance(finder.wiki_result, str)