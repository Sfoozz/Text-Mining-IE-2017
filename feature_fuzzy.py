#je moet een lusje maken over de lijst met boeken. van elk boek de titel ophalen
# en dan met str.find() naar de titel zoeken in de thread.
#str1 is dan xml-tekst en find(str2) is dan de titel van een boek
#
#Def feature_fuzzy moet doen:
#
#1. def search lists loopen over json-file: dit is input
#2. met fuzzy loopen over xml-file: nu wordt gezocht naar wat in de input zit
#3. return: zoekresultaat = titel in input, titel gevonden in bestand, ratio van overeenkomst
#


from fuzzywuzzy import fuzz
from JSON_doc_lezen import search_titles
from get_text_from_xml import get_text_from_xml

#Dit klopt dus nog niet helemaal!
title_jsondata = []
for titles in search_titles('small_corpus.json'):
    title_jsondata.append(titles)

for words in get_text_from_xml('/Users/tessavermeir/PycharmProjects/Text-Mining-IE-2017/sbs16mining-linking-training-threads_kleindeel/thread.1546.xml'):
    zoekresultaat = fuzz.partial_ratio(words, title_jsondata)

print (words, title_jsondata, zoekresultaat)

#titles in JSON:
# 1.'Succesful Slimming: Cassette',
# 2.'The Birth of Tangun: The Legend of Korea's Fist King',
# 3.'Conversations With God: An Uncommon Dialogue'

#titles in XML:
#1.Oorspronkelijk niet, heb ik zelf toegevoegd om te testen of fuzzy werkt (maar werkt dus nog niet haha)
#2.Nee
#3.Nee

#Zo ziet een fuzzy eruit:
#fuzz.ratio("this is a test", "tish is a test")
#print(fuzz.ratio("this is a test", "tish is a test"))

#fuzz.partial_ratio("this is a test", "tish is a test")
#print(fuzz.partial_ratio("this is a test", "tish is a test"))


