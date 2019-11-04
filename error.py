def checkDupSym(symTab,sym,line,errorTab,keyWords):
	for symBol in symTab:
		if sym==symBol[1]:
			tempList=[line,sym,1]
			errorTab.append(tempList)
			return 0
		if sym in keyWords and sym!="main":
			tempList=[line,sym,3]
			errorTab.append(tempList)
			return 0
	return 1
def putError(errorTab,sym,line,errorCode):
	tempList=[line,sym,errorCode]
	errorTab.append(tempList)
	return
def checkOprandError(opOne,opTwo,line,keyWords,errorTab):	
	if opOne in keywords:
		putError(errorTab,opOne,line,4)
	if opTwo in keywords:
		putError(errorTab,opTwo,line,4)
		return 0
	else:
		return 1
def checkDupLabel(symTab,sym,line,errorTab,keyWords):
	if sym in keyWords and sym!="main":
		putError(errorTab,sym,line,3)
		return 0
	else:
		for symbol in range(0,len(symTab)):
			if sym==symTab[symbol][1]:
				if symTab[symbol][7]=="U":
					symTab[symbol][7]="D"
					return 0
				else:
					putError(errorTab,sym,line,1)
					return 0
				
		return 1
