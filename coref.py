from __future__ import division
import pickle
import sys
import os

sys.path.insert(0,'./scripts/')

from rule1 import r1
from rule2 import r2
from rule3 import r3
from rule4 import r4
from rule5 import r5


with open('./scripts/pronouns/reflexives','rb') as f:
    reflexives = pickle.load(f)

with open('./scripts/pronouns/relatives','rb') as f:
    relatives = pickle.load(f)

with open('./scripts/pronouns/seconds','rb') as f:
    seconds = pickle.load(f)

with open('./scripts/pronouns/spatials','rb') as f:
    spatials = pickle.load(f)

with open('./scripts/pronouns/firsts','rb') as f:
    firsts = pickle.load(f)

total = 0
found = 0

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
            total = total +1
            if rr != "":
                found = found + 1
            print cc + '  ->  ' + rr
        print "\n\n"
    except:
        continue

accuracy = found/total*100

print "************************************"
print "\n"
print "Total Identified: " + str(total)
print "Total Found: " + str(found)
print "Accuracy: " + str(accuracy) + "%"
print "\n"
print "************************************"
