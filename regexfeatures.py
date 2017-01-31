#(pseudo)code for features

# Title volgens Brin:
/[A-Z0-9][A-Za-z0-9 .,:'#!?;&]4;45[A-Za-z0-9?!]/

wordsbefore =

/'s/
#matches everything with author/possesive before

#NB als we niet op tokens zoeken maar gewoon op wat er direct aan vooraf gaat,
#dan moeten achter alle regex nog \s


/[Rr]ead(ing)?/
/[Ff]inish(ed)?/
/[Ll]ike(d)?/
/[Ee]njoy(ed)?/
/[Ll]ov(e\ed)?/

/[Nn]ovel/
/[Bb]ook/
/[Ww]ork/
/[Ww]riting/
/[Bb]est(\s)?seller/

/[Ee]dition(\sof)?/
/[Tt]ale(\sof)?/
/[Cc]copy(\sof)?/
/[Ss]tory(\sof)?/

/[Dd]rama/
/[Nn]arrative/
/[Rr]omance/
/[Nn]ovella/
/[Vv]olume/

/[Nn]amed/
/[Cc]alled/
/([Ee]n)?titled/

/[Ll]ooking\sfor/


wordsafter =

#NB als we niet op tokens zoeken maar gewoon op wat er direct op volgt,
#dan moeten voor alle regex nog \s

/[Bb][Y]y/
/((is|was|'s)\s)?(written|authored|pennend)\sby/
   
/[Bb]ooks/
/[Ss]eries/
/[Tt]rilogy/
# bij een serie moeten we linken aan het eerste boek van een serie,
# maar dat is natuurlijk ongemogelijk

#don't know whether this is possible:
surrounded by = 
/"/ + /"/
/'/ + /'/
/&lt;i&gt;/ + /&lt;\/i&gt;/
# above is HTML voor <i> X </i> (italized book title); invalid for XML


