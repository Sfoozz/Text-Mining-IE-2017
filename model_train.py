from custom_chunker_gis import ConsecutiveNPChunker
from nltk.corpus import conll2002 as conll
from features import chunkfeatures_2

tiny_sample = 150
# training = conll.chunked_sents("ned.train")  # Train with full dataset
training = conll.chunked_sents("ned.train")[:tiny_sample] # SHORT DATASET: FOR DEMO/DEBUGGING ONLY! 
testing = conll.chunked_sents("ned.testa")

simple_nl_NER = ConsecutiveNPChunker(chunkfeatures_2, training)

from custom_chunker import ConsecutiveNPChunker
from features import chunkfeatures_2

myRecognizer = ConsecutiveNPChunker(chunkfeatures_2, training)

import pickle
output = open("best.pickle", "wb")
pickle.dump(myRecognizer, output, 2)
output.close()
