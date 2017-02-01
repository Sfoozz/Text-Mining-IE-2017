import nltk
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk import MultiParentedTree
from nltk import ParentedTree
from nltk.parse.stanford import StanfordParser
import os
import re

java_path = "C:/Program Files (x86)/Java/jre1.8.0_111/bin/java.exe" #specific for my computer
os.environ['JAVAHOME'] = java_path
path_to_jar = '.\stanford-parser-full-2016-10-31\stanford-parser.jar'
path_to_models_jar = '.\stanford-parser-full-2016-10-31\stanford-parser-3.7.0-models.jar'
parser = StanfordParser(path_to_jar=path_to_jar, path_to_models_jar=path_to_models_jar)

def tagging(dictionary):
    """Takes a dictionary of {post id: sentence}
    and returns a dictionary of post id's and
    tokenized and tagged sentences."""

    post_dict = {}

    for postid, post in dictionary.items():
        postlist = []
        sents = sent_tokenize(post)
        for sent in sents:
            newsent = re.sub(r"[\(|\)]", "", sent)  # remove brackets because they mess up the parsing
            postlist.append(nltk.pos_tag(word_tokenize(newsent)))

        post_dict[postid] = postlist

    return post_dict

def parsing(sentence):
    """Takes a tagged sentence (lists of tuples)
    and returns the sentences parsed."""

    iter_tree = parser.tagged_parse(sentence)
    for tree in iter_tree:
        ptree = ParentedTree.convert(tree)

    return ptree