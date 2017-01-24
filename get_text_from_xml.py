import os
import xml.dom.minidom
import re
re.UNICODE

def get_text_from_xml_files(folder):
    thread_files = {}
    for filename in os.listdir(folder):
        print("Thread no. %s" % filename)
        file = folder + "/" + filename
        text = get_text_from_xml(file)
        thread_files[filename] = text;
    return thread_files

chars_to_remove = {ord(c):None for c in [u'\n', u'.', u'!', u'?']}

def get_text_from_xml(file):

    # hierin alle <text> elementen verzamelen
    alle_text = []

    # Lees xml bestand in het geheugen. je moet het document zien als een boom met <thread> als de stam
    # De takken aan de stam zijn <message> -es en die hebben weer een <text> element
    DOMTree = xml.dom.minidom.parse(file)
    collection = DOMTree.documentElement

    # text_nodelist is de lijst van alle <text> elementen.
    # het xml document wordt gefilterd eigenlijk, alle elementen van het type <text> worden er uit gehaald
    # en komen in de variabele text_nodelist terecht
    text_nodelist = collection.getElementsByTagName("text")

    # Ga alle text_node 's af en stop de text in alle_text
    for text_node in text_nodelist:
        text = text_node.childNodes[0].data
        alle_text.append(text)

    # verwijder overbodige characters
    resultaat = ' '.join(alle_text).translate(chars_to_remove)

    return resultaat

text_from_xml_files = get_text_from_xml_files("./sbs16mining-linking-training-threads_kleindeel")
for thread_file in text_from_xml_files.keys():
    print ">>>> File: %s" % thread_file
    print (''.join(text_from_xml_files[thread_file]))