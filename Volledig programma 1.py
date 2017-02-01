##########DIT WERKT NOG NIET##############

from get_text_from_xml_3  import get_text_from_xml
from pipeline_unpacked import tagging
from pipeline_unpacked import parsing
import re
import fuzzy1

def find_title(folder, metadata_json, ratio):

    for filename in os.listdir(folder):

        file = folder + "/" + filename
        postdict = get_text_from_xml(file)
        tagged = tagging(postdict)

        for postid, post in tagged.items():
            for sentence in post:
                parsed = parsing(sentence)
                subtree_features(parsed)

            ########INSERT FEATURES HERE#########

            ########INSERT GRAMMATICAL FEATURES HERE########
            # only posts that have one of the features mentioned,
            # will be retained in the dictionary.

        ##########DIT WERKT NOG NIET##############
        fuzzy_match(postdict, metadata_json, ratio)
        ##########DIT WERKT NOG NIET##############






