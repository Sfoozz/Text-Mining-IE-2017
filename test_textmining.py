import json

with open('corpus_goed.json') as json_data:
    d = json.load(json_data)
    eerste = d[0]
    print(eerste)
    eerstevalue = eerste['workID']
    print(eerstevalue)

