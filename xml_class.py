import re
re.UNICODE
import xml.dom.minidom
import os
from get_text_from_xml_new import get_text_from_xml

class XML:

    def __init__(self, file):

        xml = get_text_from_xml(file)
        self.key = xml[dict.keys(file)]
        self.value = xml[dict.values(file)]

    def __str__(self):
        return "XML [ %s, %s ]" % (self.key, self.value)

    def get_text_from_xml_files(self, folder):
        thread_files = {}
        for filename in os.listdir(folder):
            file = folder + "/" + filename
            text = get_text_from_xml(file)
            thread_files[filename] = text
        return thread_files

    def get_text_from_xml(self, file):

        alle_text = {}

        DOMTree = xml.dom.minidom.parse(file)
        collection = DOMTree.documentElement

        text_nodelist = collection.getElementsByTagName("text")
        postid_nodelist = collection.getElementsByTagName("postid")

        for text_node, postid_node in zip(text_nodelist, postid_nodelist):
            postid = postid_node.childNodes[0].data
            text = text_node.childNodes[0].data

            alle_text[postid] = text

        return (alle_text)

def read_xml_file():
    xml_files = {}
    xml_threads_data = 'sbs16mining-linking-training-threads_kleindeel/thread.1546.xml'
    with open(xml_threads_data, 'r') as f:
        for text in f:
            xml_files[text] = XML
    return xml_files

xml_class_test = read_xml_file()
print(xml_class_test)
