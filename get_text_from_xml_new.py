import xml.dom.minidom
import re
import os
re.UNICODE

def get_text_from_xml_files(folder):
    thread_files = {}
    for filename in os.listdir(folder):
        file = folder + "/" + filename
        text = get_text_from_xml(file)
        thread_files[filename] = text
    return thread_files

chars_to_remove = {ord(c):' ' for c in [u'\n', u'.', u'!', u'?', u'#', u'-', u',']}

def get_text_from_xml(file):

    alle_text = []

    DOMTree = xml.dom.minidom.parse(file)
    collection = DOMTree.documentElement

    text_nodelist = collection.getElementsByTagName("text")

    for text_node in text_nodelist:
        text = text_node.childNodes[0].data

        no_chars = text.translate(chars_to_remove)
        no_num = re.sub('\d+', '', no_chars)
        no_space = re.sub(' +', ' ', no_num)

        alle_text.append(no_space)

    return(alle_text)

