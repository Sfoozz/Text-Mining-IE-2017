#using a tagger try-out
import nltk
from nltk import word_tokenize
from get_text_from_xml_new import get_text_from_xml_files
import re
re.UNICODE

def feature_pos(folder):
    thread_files = get_text_from_xml_files(folder)
    for thread in thread_files.values():
        for message in thread:
            woorden = word_tokenize(message)
            tagged = nltk.pos_tag(woorden)
            print(tagged)

            chunked = nltk.ne_chunk(tagged, binary=True)
            print(chunked)

feature_pos(".\sbs16mining-linking-training-threads_kleindeel")