from rule1 import r1
from rule2 import r2
from rule3 import r3
from rule4 import r4
from rule5 import r5

import pickle
import sys
import os

with open('./pronouns/reflexives','rb') as f:
    reflexives = pickle.load(f)

with open('./pronouns/relatives','rb') as f:
    relatives = pickle.load(f)

with open('./pronouns/seconds','rb') as f:
    seconds = pickle.load(f)

with open('./pronouns/spatials','rb') as f:
    spatials = pickle.load(f)

with open('./pronouns/firsts','rb') as f:
    firsts = pickle.load(f)

for f in os.listdir("DATA/PROCESSED-DATA/collection/"):
    res=[]
    try:
        ofile = open("DATA/PROCESSED-DATA/collection/" + f,"rb")
        var = pickle.load(ofile)
        print "Text:\n"

        for i in var.globalWordList:
            sys.stdout.write(i.word)
        
        print "\n"

        r1(var,res,reflexives)
        r2(var,res,spatials)
        r3(var,res,relatives)
        r4(var,res,firsts)
        r5(var,res,seconds)
        
        print "Analysis:\n"
        
        for entry in res:
            s = var.sentenceList[entry['sentence']]
            c = s.chunkList[entry['pronoun']]
            r = []
            for i in entry['referents']:
                r.append(s.chunkList[i])

            cc = "".join([var.globalWordList[i].word for i in c.wordNumList])
            rr = ""
            try:
                rr = "".join([var.globalWordList[i].word for i in r[0].wordNumList])
            except:
                pass
            print cc + '->' + rr
        print "\n\n"
    except:
        continue
