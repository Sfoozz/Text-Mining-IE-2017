#dit zijn alle stukjes die ik tot nu toe geschreven heb, maar er zijn nog wel een paar problemen.

def read_data(json_file): #directory to file
    """Opens a JSON-file, reads it line by line
    to create a list of all the elements in the
    file."""
    
    data = []
    with open(json_file) as f:
        for line in f:
            data.append(json.loads(line))
    f.close()
    
    return data

def count_versions(json_file):
    """Takes the output of read_data() to count
    the amount of books that have more than
    one version."""
    data = read_data(json_file)
    for book in data:
        if len(book["versions"]) > 1:
            n += 1
    if n == 0:
        print("Every book has exactly one version.")
    else:
        print(str(n), "books have more than one version.")

def search_lists(json_file):
    """Takes the output of read_data() to produce
    easily managable lists of data to be able to
    search for its contents in other text files. It
    returns:
    1. a list 'titles_workids' of dictionaries that have
    the title as key and the workID as its value;
    2. a list 'titles'of just the book titles."""

    data = read_data(json_file)
    
    titles_workids = []
    titles = []
    for book in data:
        book_and_version = {}

        for version in book["versions"]:
            book_and_version[version["booktitle"]] = book["workID"]
            titles.append(version["booktitle"])

        titles_workids.append(book_and_version)

    return titles_workids
    return titles

def get_text_from_xml(folder): #directory to folder
    """This function takes a folder with xml-files from
    LibraryThing and prints an overview of the threads and
    messages - DON'T USE FOR FULL CORPORA"""

    import os
    from xml.dom.minidom import parse
    import xml.dom.minidom

    n = 1

    for filename in os.listdir(folder):
        print("Thread no. ", str(n), "\n")
        m = 1

        file = folder + "/" + filename #Loop over all the files in the folder

        # Open XML document using minidom parser
        DOMTree = xml.dom.minidom.parse(file)
        collection = DOMTree.documentElement

        text_nodelist = collection.getElementsByTagName("text")

        while m <= len(text_nodelist):

            text_node = text_nodelist[m-1]
            text = text_node.childNodes[0].data

            print("*****POST no.", str(m),"*****\n", text)

            m += 1

        n += 1

def first_attempt_at_match(folder):
    """This is a first try to match titles with occurrences
    in the corpus. It does not work yet, since it only prints
    "Mozart" with a few specific posts. It is an adaptation of
    get_text_from_xml()."""

    import os
    from xml.dom.minidom import parse
    import xml.dom.minidom

    n = 1

    for filename in os.listdir(folder):
        print("Thread no. ", str(n), "\n")

        m = 1

        file = folder + "/" + filename  # Loop over all the files in the folder

        # Open XML document using minidom parser
        DOMTree = xml.dom.minidom.parse(file)
        collection = DOMTree.documentElement

        text_nodelist = collection.getElementsByTagName("text")

        while m <= len(text_nodelist):

            text_node = text_nodelist[m - 1]
            text = text_node.childNodes[0].data

            for title in titles:
                if title in text:
                    print("*****POST no.", str(m), "*****\n")
                    print(title, "\n", text)

            m += 1

        n += 1

