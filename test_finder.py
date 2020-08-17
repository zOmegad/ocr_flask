import finder as script
import pytest

# test that wiki api returns objects
def test_wiki_result():
	finder = script.Finder()
	finder.resultat = "Paris"
	finder.wiki()

	assert isinstance(finder.wiki_result, str)
	assert isinstance(finder.coo_x, float)
	assert isinstance(finder.coo_y, float)

# test cutter functiun
def test_cutter_return():
	awnser = "Ou se trouve le zoo de Paris ?"
	result = "zoo paris "

	finder = script.Finder()
	finder.cutter(awnser)
	assert result == finder.resultat