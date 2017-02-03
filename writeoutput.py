
#writing output:
#comma-separated values in text (can be easily exported to excel)

outfile = open("output.txt", "w")

#deze def kan dan worden aangeroepen bij een match
def writeresult(threadid, postid, workid):
    outfile.write(threadid)
    outfile.write(",")
    outfile.write(postid)
    outfile.write(",")
    outfile.write(workid)
    outfile.write("\n")

# hier moet natuurlijk nog een for-loopje per gevonden boektitel, maar voor nu:
threadid = "1111"
postid = "1"
workid = "123456789"

writeresult(threadid, postid, workid)
writeresult(threadid, postid, workid)
writeresult(threadid, postid, workid)

#dit moet dan in het totale programma uiteindelijk op het eind
outfile.close()
