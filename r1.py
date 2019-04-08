def r1():
     ...:     sc=[]
     ...:     for word in dat.globalWordList:
     ...:         if word.word in reflexives:
     ...:             sc.append([word.sentenceNum,word.chunkNum,dat.globalWordList.index(word)])
     ...:     for pro in sc:
     ...:         flag=1
     ...:         s=dat.sentenceList[pro[0]]
     ...:         node=s.nodeDict[s.chunkList[pro[1]].nodeName]
     ...:         x=s.nodeDict[node.nodeParent]
     ...:         while(x.nodeName[:3]!='VGF' and x.nodeName[:2]!='NP'):
     ...:             x=s.nodeDict[x.nodeParent]
     ...:         if(x.nodeName[:2]=='NP'):
     ...:             for child in x.childList:
     ...:                 if s.nodeDict[child].nodeRelation=='r6' and s.nodeDict[child]!=node:
     ...:                     flag=0
     ...:                     for chunk in s.chunkList:
     ...:                         if chunk.nodeName==child:
     ...:                             ans.append([dat.globalWordList[pro[2]].word, "".join([dat.globalWordList[i].word for i in chunk.wordNumList])])
     ...:         if(flag):
     ...:             while(x.nodeName[:3]!='VGF'):
     ...:                 x=s.nodeDict[x.nodeParent]
     ...:                 print x.nodeName
     ...: 
     ...:             for child in x.childList:
     ...:                 if s.nodeDict[child].nodeRelation=='k1' and s.nodeDict[child]!=node:
     ...:                     flag=0
     ...:                     for chunk in s.chunkList:
     ...:                         if chunk.nodeName==child:
     ...:                             ans.append([dat.globalWordList[pro[2]].word, "".join([dat.globalWordList[i].word for i in chunk.wordNumList])])
     ...: 
     ...:             if(flag):
     ...:                 x=s.nodeDict[x.nodeParent]
     ...:             if(x.nodeName[:3]=='CCP' and x.nodeRelation=='k1'):
     ...:                 for child in x.childList:
     ...:                     if s.nodeDict[child].nodeName[:2]=='NP':
     ...:                         for chunk in s.chunklist:
     ...:                             if chunk.nodeName==child:
     ...:                                 ans.append([dat.globalWordList[pro[2]].word, "".join([dat.globalWordList[i].word for i in chunk.wordNumList])])

