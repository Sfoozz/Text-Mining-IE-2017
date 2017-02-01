import re
from feature_fuzzy import feature_fuzzy2
#from book import read_book_list

def text():
    conn = open("testtext.txt", "r")
    text = conn.read()
    conn.close()

    # lines are full posts: <text> ... </text>
    lines = text.splitlines()

    return lines

def research_sents():
    sents = []
    for line in text():
        if re.search("\sby\s", line):                   #searches for 'by'
            sents.append(line)
        if re.search("\s[Rr]ead(ing)?\s", line):        #searches for 'read(ing)'
            sents.append(line)
        if re.search("\s[Ff]inish(ed)?\s", line):       #searches for 'finish(ed)'
            sents.append(line)
        if re.search("\s[Ll]ike(d)?\s", line):          #searches for 'like(d)'
            sents.append(line)
        if re.search("\s[Ee]njoy(ed)?\s", line):        #searches for 'enjoy(ed)'
            sents.append(line)
        if re.search("\s[Ll]ove(d)?\s", line):          #seraches for 'love(d)'
            sents.append(line)
        if re.search("\s[Nn]ovel(s)?\s", line):         #searches for 'novel'
            sents.append(line)
        if re.search("\s[Bb]ook(s)?\s", line):          #searches for 'books'
            sents.append(line)
        if re.search("\s[Ww]ork\s", line):              #searches for 'work'
            sents.append(line)
        if re.search("\s[Ww]riting\s", line):           #searches for 'line'
            sents.append(line)
        if re.search("\s[Bb]est(\s)?seller\s", line):   #searches for '(best) seller'
            sents.append(line)
        if re.search("\s[Ee]dition(\sof)?\s", line):    #searches for 'edition (of)'
            sents.append(line)
        if re.search("\s[Tt]ale(\sof)?\s", line):       #searches for 'tale (of)'
            sents.append(line)
        if re.search("\s[Cc]opy(\sof)?\s", line):        #searches for 'copy (of)'
            sents.append(line)
        if re.search("\s[Ss]tory(\sof)?\s", line):      #searches for 'story (of)'
            sents.append(line)
        if re.search("\s[Dd]rama\s", line):             #searches for 'drama'
            sents.append(line)
        if re.search("\s[Nn]arrative\s", line):         #searches for 'narrative'
            sents.append(line)
        if re.search("\s[Rr]omance\s", line):           #searches for 'romance'
            sents.append(line)
        if re.search("\s[Nn]ovella\s", line):           #searches for 'novella'
            sents.append(line)
        if re.search("\s[Vv]olume\s", line):            #searches for 'volume'
            sents.append(line)
        if re.search("\s[Nn]amed\s", line):             #searches for 'named'
            sents.append(line)
        if re.search("\s[Cc]alled\s", line):            #searches for 'called'
            sents.append(line)
        if re.search("\s([Ee]n)?titled\s", line):       #searches for '(en)titled'
            sents.append(line)
        if re.search("\s[Ll]ooking\sfor\s", line):      #searches for 'looking for'
            sents.append(line)

    return sents

aantalzinnen = len(research_sents())
print(aantalzinnen, research_sents())

titels = feature_fuzzy2(research_sents())
print(titels)
