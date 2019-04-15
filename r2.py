import os
import pickle

with open('./pronouns/spatials','rb') as f:
    spatials = pickle.load(f)

def r2():
    sc=[]
    for word in var.globalWordList:
        if word.word in spatials:
            sc.append([word.sentenceNum, word.chunkNum])
    for _ in sc:
        s = var.sentenceList[_[0]]
        c = s.chunkList[_[1]]
        n = s.nodeDict[c.nodeName]
        fans={}
        fans['sentence'] = _[0]
        fans['pronoun'] = _[1]
        fans['referents'] = []
        flag = 1
        limit=3
        while(flag and limit):
            for chunk in s.chunkList:
                if chunk.nodeName[:2] == 'NP' and s.nodeDict[chunk.nodeName].nodeRelation == 'k7p' and s.nodeDict[chunk.nodeName] != n:
                    fans['referents'].append(chunk.chunkNum)
                    flag=0
                    break
            try:
                s = var.sentenceList[_[0]-1]
                limit=limit-1
            except:
                break
        res.append(fans)

for f in os.listdir("DATA/PROCESSED-DATA/collection/"):
    res=[]
    try:
        ofile=open("DATA/PROCESSED-DATA/collection/"+f,"rb")
        var=pickle.load(ofile)    
        r2()

        for entry in res:
            s = var.sentenceList[entry['sentence']]
            c = s.chunkList[entry['pronoun']]
            r = []
            for i in entry['referents']:
                r.append(s.chunkList[i])

            cc = "".join([var.globalWordList[i].word for i in c.wordNumList])
            rr = "".join([var.globalWordList[i].word for i in r[0].wordNumList])
            print cc + " -> " + rr

    except:
        continue
