def chunkfeatures_1(sentence, i, history):
    """Simplest chunker features: Just the POS tag of the word""" 
    word, pos = sentence[i]
    return { "pos": pos }

def chunkfeatures_2(sentence, i, history):
    """Simplest chunker features: Just the POS tag of the word""" 
    features = {}
    word, pos = sentence[i]
    features['pos'] = pos
    features['word'] = word
    if word[0].isupper():
        features['startswithcapital'] = True
    else:
        features['startswithcapital'] = False
    if word.isupper():
        features['allcaps'] = True
    else:
        features['allcaps'] = False
    if i == 0:
        prevword, prevpos = '<START>', '<START>'
    else:
        prevword, prevpos = sentence[i-1]
    features['prevpos'] = prevpos
    return features
