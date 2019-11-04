import error as ERR
def check(operand,symTab):
	for i in range(0,len(symTab)):
		if operand==symTab[i][1]:
			return i 
	return 0
def checkLit(lit,litTab):
	for h in range(0 ,len(litTab)):
		if lit==litTab[h][1]:
			return 0
	return 1
def checkAdd(tempStr,regTab,symTab,litTab,errorTab,size,litNo,lineNo):
	operSplit=tempStr[1].split(',')
	if operSplit[0] in regTab and operSplit[1] in regTab:
		size+=2
		return litNo
	elif operSplit[0] in regTab and operSplit[1].isdecimal():
		size+=3
		if checkLit(operSplit[1],litTab):
			litNo+=1
			litList=[litNo,operSplit[1],(hex(int(operSplit[1])))[2:].upper()]
			litTab.append(litList)
			return litNo
		return litNo
	elif operSplit[0] in regTab and check(operSplit[1],symTab):
				size+=6
				return litNo
	else:
		ERR.putError(errorTab,'',lineNo,4)
		return litNo
def checkMov(tempStr,regTab,symTab,litTab,errorTab,size,litNo,lineNo):
	operSplit=tempStr[1].split(',')
	if operSplit[0] in regTab and operSplit[1] in regTab:
		size+=2
		return litNo
	elif operSplit[0] in regTab and operSplit[1].isdecimal():
		size+=5
		if checkLit(operSplit[1],litTab):
			litNo+=1
			litList=[litNo,operSplit[1],(hex(int(operSplit[1])))[2:].upper()]
			litTab.append(litList)
			return litNo
		return litNo
	elif operSplit[0] in regTab and check(operSplit[1],symTab):
				size+=5
				return litNo
	else:
		ERR.putError(errorTab,'',lineNo,4)
		return litNo
def checkInc(tempStr,regTab,symTab,errorTab,size,lineNo):
	if tempStr[1] in regTab:
		size+=2
	elif "dword" in tempStr[1]:
		size+=6	
	else:
		ERR.putError(errorTab,'',lineNo,4)
def checkJmp(tempStr,regTab,symTab,errorTab,size,lineNo,keyWords,i):
	if tempStr[1] in keyWords:
		ERR.putError(errorTab,tempStr[1],line,4)
		return i
	elif (check(tempStr[1],symTab))==0:
		i=i+1
		emptyList=[i,tempStr[1],0,'t','','','','U',lineNo]
		symTab.append(emptyList)
		size+=2
		return i
	else:
		size+=2
		return i
