"""Fuzzywuzzy is een zoekexpressie die teksten geheel of gedeeltelijk matcht; met fuzz.partial_ratio kun je zien
in hoeverre twee strings met elkaar matchen. Dit is een handige zoekfunctie voor forumposts, omdat niet iedereen
de boektitels op dezelfde manier schrijft. Met fuzzy worden alle varianten toch makkelijk gevonden.

Feature_fuzzy maakt gebruik van de class Book (zie book.py) en de keys van get_text_from_xml
(zie get_text_from_xml_new.py); hij loopt over de books met de def read_book_list() en kijkt in hoeverre dit matcht
met de text in de xml-threads."""

from fuzzywuzzy import fuzz
from get_text_from_xml_new import get_text_from_xml
from book import read_book_list

def feature_fuzzy(file):
    for book in read_book_list():
        zoekresultaat = fuzz.partial_ratio (book.title, dict.keys(get_text_from_xml(file)))
        if zoekresultaat > 50:
            return[zoekresultaat, book]
        else:
            return []
