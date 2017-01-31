import json

class Book:

    def __init__(self, jsonText):
        book = json.loads(jsonText)
        self.workdID = book["workID"]
        version = book['versions'][0]
        self.author = version["author"]
        self.isbn = version["ISBN"]
        self.title = version["booktitle"]

    def __str__(self):
        return "Book [ %s, %s, %s, %s ]" % (self.workdID, self.author, self.isbn, self.title)

book = Book ('{"workID": "7494673", "versions": [{"author": "", "ISBN": "0000000140", "booktitle": "Ca 1-Part 7 Lincoln"}]}')
#print (book)
#print ("workID: %s" % book.workdID)

def read_book_list():
    books = []
    book_metadata_json = 'small_corpus.json'
    # book_metadata_json = '/Users/jan/Downloads/sbs16mininsbs16mining.book-metadata.json'
    with open(book_metadata_json, 'r') as f:
        for line in f:
            books.append(Book(line))
    return books

