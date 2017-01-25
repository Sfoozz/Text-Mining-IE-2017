import pickle
import nltk
ner = pickle.load(open(r"C:\Users\Sophie\best.pickle", "rb"))

from nltk.corpus import conll2002 as conll

# Usage 1: parse a list of sentences
tagzinnen = conll.tagged_sents("ned.train")[1000:1050]
result = ner.parse_sents(tagzinnen)

# Usage 2: self-evaluate
chunkzinnen = conll.chunked_sents("ned.testa")[1000:1500]
print(ner.evaluate(chunkzinnen))
