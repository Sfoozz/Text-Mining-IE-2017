#even proefje met re.search door posts, werkt.
#weet alleen nog niet hoe dan alleen een titel oid te selecteren
#daarvoor hebben we eerst NE's nodig

conn = open("testtext.txt", "r")
text = conn.read()
conn.close()

#lines are full posts: <text> ... </text>
lines = text.splitlines()

import re

#example: list with all lines with 'by'
sents = []
for line in lines:
    if re.search("\sby\s", line):
        sents.append(line)


#writing output:
#comma-separated values in text (can be easily exported to excel)

outfile = open("output.txt", "w")

# hier moet natuurlijk nog een for-loopje per gevonden boektitel, maar voor nu:
threadid = "3108"
postid = "1"
workid = "123456789"

outfile.write(threadid)
outfile.write(",")
outfile.write(postid)
outfile.write(",")
outfile.write(workid)
outfile.write("\n")

outfile.close()


#re.search for "read(ing) TITLE/anyotherstringwith capitals"
#[Rr]ead(ing)?\s[A-Z0-9][A-Za-z0-9 .,:'#!?;&]4;45[A-Za-z0-9?!]

