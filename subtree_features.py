import re
from nltk import ParentedTree
from nltk import Tree

def subtree_features(parsed):
    """Takes a tree and returns a list of the text
    that needs to be analyzed by fuzzy"""

    for subtree in parsed.subtrees():
        leaves = " ".join(subtree.leaves())
        if subtree.label() == r"VB":
            if re.search(r"[Rr]ead(ing)?", leaves):
                print(leaves)
        if subtree.label() == r"NP":
            if re.search(r"by", leaves):
                print(leaves)