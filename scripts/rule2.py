def r2(var,res,li):
    sc=[]
    for word in var.globalWordList:
        if word.word in li:
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
