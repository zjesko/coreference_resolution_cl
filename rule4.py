complementizer = u'\u0915\u093f'

def r4(var,res,li):
    sc=[]
    for word in var.globalWordList:
        if word.word in li:
            sc.append([word.sentenceNum, word.chunkNum])
    for _ in sc:
        s = var.sentenceList[_[0]]
        c = s.chunkList[_[1]]
        n = s.nodeDict[c.nodeName]
        x = s.nodeDict[n.nodeParent]
        fans={}
        fans['sentence'] = _[0]
        fans['pronoun'] = _[1]
        fans['referents'] = []
        flag = 1
        while(flag):
            if var.globalWordList[s.chunkList[x.chunkNum].wordNumList[0]].word == complementizer:
                x = s.nodeDict[x.nodeParent]
                if x.nodeName[:1] == 'V':
                    for child in x.childList:
                        if s.nodeDict[child].nodeRelation == 'k1':
                            fans['referents'].append(s.nodeDict[child].chunkNum)
                            flag = 0
                else:
                    break
            if x.nodeParent == "None":
                break
            x = s.nodeDict[x.nodeParent]
        res.append(fans)

