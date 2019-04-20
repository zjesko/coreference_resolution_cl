def r3(var,res,li):
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
            if x.nodeName[:3] == 'VGF' or x.nodeName[:4] == 'VGNF':
                if x.nodeRelation == 'nmod__relc':
                    fans['referents'].append(s.nodeDict[x.nodeParent].chunkNum)
                    flag = 0
            if x.nodeParent == "None":
                break
            x = s.nodeDict[x.nodeParent]
        res.append(fans)
