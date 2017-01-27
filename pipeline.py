import nltk
from nltk import word_tokenize
from nltk import sent_tokenize
from nltk.parse.stanford import GenericStanfordParser
from get_text_from_xml_3 import get_text_from_xml_files
import re
import os
re.UNICODE

java_path = "C:/Program Files (x86)/Java/jre1.8.0_111/bin/java.exe" #specific for my computer
os.environ['JAVAHOME'] = java_path
path_to_jar = '.\stanford-parser-full-2016-10-31\stanford-parser.jar'
path_to_models_jar = '.\stanford-parser-full-2016-10-31\stanford-parser-3.7.0-models.jar'

parser = parse_sents(path_to_jar=path_to_jar, path_to_models_jar=path_to_models_jar)

def pipeline_tagging(folder):
    """Iterates over the dictionaries to split into sentences,
    tokenize into words and POS-tag the words from each post.
    Simultaneously collects all the tagged words into sentences,
    sentences into posts and recreates a similar dictionary as
    before only with tagged words."""

    thread_files = get_text_from_xml_files(folder)
    thread_files_tagged = {}

    for threadid, thread in thread_files.items():
        post_dict_list = []

        for postid, post in thread.items():
            post_dict = {}
            postlist = []
            sents = sent_tokenize(post)

            for sent in sents:
                postlist.append(nltk.pos_tag(word_tokenize(sent)))

            post_dict[postid] = postlist

            post_dict_list.append(post_dict)

        thread_files_tagged[threadid] = post_dict_list

    return thread_files_tagged

def pipeline_parsing(folder):
    """Takes the tagged files and parses them with the
    Stanford CoreNLP parser. For now: prints tree. Needs
    to be changed later on."""

    thread_files_tagged = pipeline_tagging(folder)
    for threadid, thread in thread_files_tagged.items():
        for posts in thread:
            for post in posts.values():
                tree = parser.tagged_parse_sents(post)

                for sentence in tree:
                    for line in sentence:
                        print(line)

