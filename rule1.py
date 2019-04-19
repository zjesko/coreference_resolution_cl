def r1(var,res,li):
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
            if x.nodeName[:2] == 'NP':
                for child in x.childList:
                    if s.nodeDict[child].nodeRelation == 'r6' and s.nodeDict[child].nodeName != n.nodeName:
                        fans['referents'].append(s.nodeDict[child].chunkNum)
                        flag = 0
            elif x.nodeName[:3] == 'VGF':
                for child in x.childList:
                    if s.nodeDict[child].nodeRelation == 'k1' and s.nodeDict[child].nodeName != n.nodeName:
                        fans['referents'].append(s.nodeDict[child].chunkNum)
                        flag = 0
            elif x.nodeName[:3] == 'CCP' and x.nodeRelation == 'k1':
                for child in x.childList:
                    if s.nodeDict[child].nodeName[:2] == 'NP' and s.nodeDict[child].nodeName != n.nodeName:
                        fans['referents'].append(s.nodeDict[child].chunkNum)
                        flag = 0
            if x.nodeParent == "None":
                break
            x = s.nodeDict[x.nodeParent]
        res.append(fans)
