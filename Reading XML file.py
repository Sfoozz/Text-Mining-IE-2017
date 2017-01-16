import os
from xml.dom.minidom import parse
import xml.dom.minidom

folder = r"./sbs16mining-linking-training-threads_kleindeel"  # took a sample of the training data so my computer wouldn't explode
n = 1

for filename in os.listdir(folder):
    file = folder + "/" + filename #Loop over all the files in the folder

    # Open XML document using minidom parser
    DOMTree = xml.dom.minidom.parse(file)
    collection = DOMTree.documentElement

    messages = collection.getElementsByTagName("text")[0]

    print("thread no.", n, ":", messages.childNodes[0].data, "\n")

    n += 1 #only for the message
