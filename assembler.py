import error as ERR
import firstPass as PASS
import secondpass as P2
symTab=[]
errorTab=[]
litTab=[]
regTab=["eax","ecx",'edx',"ebx",'esp',"ebp","esi","edi"]
keyWords=['eax','ecx','ebx','edx','esp','ebp','esi','edi','mov','add','main','dd','db','dw','dq','resb','resw','resd']
errorDict={1:"error:symbol redefined",2:"error:symbol undefined",3:"error:keyword is used as an identifier",4:"error:invalid use of opcode and operands"}
def readFile(filename):
	dflag=0
	bflag=0
	tflag=0
	i=0
	litNo=0
	lineNo=1
	size=0
	fp=open(filename,"r")
	for j in fp:
		if "section .data" in j:
			size=0
			dflag=1
			lineNo+=1
		elif "section .bss" in j:
			size=0
			dflag=0
			bflag=1
			lineNo+=1
		elif "section .text" in j:
			size=0
			dflag=0
			bflag=0
			tflag=1
			lineNo+=1
		elif "db" in j and dflag==1:
			str5=''
			str1=j.split('"')
			str2=str1[0].split()
			str3=str1[2].split(",")
			if ERR.checkDupSym(symTab,str2[0],lineNo,errorTab,keyWords):
				i+=1
				emptyList=[i,str2[0],(hex(size))[2:].upper(),'d',1]
				str3.remove('')
				length=len(str1[1])+len(str3)	
				emptyList.append(length)
				size=size+length
				for k in range(0,len(str1[1])):
					str5=str5+(hex(ord(str1[1][k:k+1]))[2:])
				str5=str5+hex(int(str3[0]))[2:]+hex(int(str3[1].rstrip()))[2:]
				emptyList[7:]=[str5.upper(),'D',lineNo]
				symTab.append(emptyList) 
			lineNo+=1
		elif dflag==1:
			str1=j.split()
			list1=list()
			if ERR.checkDupSym(symTab,str1[0],lineNo,errorTab,keyWords):	
				i+=1
				emptyList=[i,str1[0],(hex(size))[2:].upper(),'d']
				str2=str1[2].split(",")
				for k in str2:
					list1.append((hex(int(k)))[2:])
				if str1[1]=="dd":
					emptyList.append(4)
					size=size+len(list1)*4
				elif str1[1]=="dw":
					emptyList.append(2)
					size=size+len(list1)*2
				elif str1[1]=="dq":
					emptyList.append(8)
					size=size+len(list1)*8
				constr=''
				for h in list1:
					constr=constr+h
				emptyList[5:]=[len(list1),constr.upper(),"D",lineNo]
				symTab.append(emptyList)
			lineNo+=1
		elif bflag==1:	
			str1=j.split()
			if ERR.checkDupSym(symTab,str1[0],lineNo,errorTab,keyWords):
				i+=1
				emptyList=[i,str1[0],(hex(size))[2:].upper(),'b']
				if str1[1]=="resd":
					size=size+4*int(str1[2])
					emptyList.append(4*int(str1[2]))
				elif str1[1]=="resb":
					size=size+int(str1[2])
					emptyList.append(1*int(str1[2]))
				elif str1[1]=="resw":
					size=size+2*int(str1[2])
					emptyList.append(2*int(str1[2]))
				elif str1[1]=="resq":
					size=size+8*int(str1[2])
					emptyList.append(8*int(str1[2]))
				emptyList[5:]=['','','D',lineNo]
				symTab.append(emptyList)
			lineNo+=1
		elif tflag==1:
			if "extern" in j:
				str1=j.split()[1].split(",")
				for x in str1:
					if ERR.checkDupSym(symTab,x,lineNo,errorTab,keyWords):
						i+=1
						emptyList=[i,x,'','t','','','','U',lineNo]
						symTab.append(emptyList)
				lineNo+=1
			elif "golbal main"in j:
				lineNo+=1
			else:
				size=0
				tempStr=j.split()
				if len(tempStr)==1 and ":" not in tempStr[0]:
					ERR.putError(errorTab,'',lineNo,4)
					lineNo+=1
				elif ":" in tempStr[0]:
					splitStr=tempStr[0].split(':')
					if ERR.checkDupLabel(symTab,splitStr[0],lineNo,errorTab,keyWords):
						i+=1
						emptyList=[i,splitStr[0],0,'t','','','','D',lineNo]
						symTab.append(emptyList)
					if splitStr[1]=='mov':
						litNo=PASS.checkMov(tempStr,regTab,symTab,litTab,errorTab,size,litNo,lineNo)
						lineNo+=1
					elif splitStr[1]=='add':
						litNo=PASS.checkAdd(tempStr,regTab,symTab,litTab,errorTab,size,litNo,lineNo)
						lineNo+=1
					elif splitStr[1]=='inc':
						PASS.checkInc(tempStr,regTab,symTab,errorTab,size,lineNo)
						lineNo+=1
					elif splitStr[1]=='jmp':
						i=PASS.checkJmp(tempStr,regTab,symTab,errorTab,size,lineNo,keyWords,i)
						lineNo+=1
					else:
						lineNo+=1
				elif tempStr[0]=='mov':
					litNo=PASS.checkMov(tempStr,regTab,symTab,litTab,errorTab,size,litNo,lineNo)
					lineNo+=1
				elif tempStr[0]=='add':
					litNo=PASS.checkAdd(tempStr,regTab,symTab,litTab,errorTab,size,litNo,lineNo)
					lineNo+=1	
				elif tempStr[0]=='inc':
					PASS.checkInc(tempStr,regTab,symTab,errorTab,size,lineNo)
					lineNo+=1
				elif tempStr[0]=='jmp':
					i=PASS.checkJmp(tempStr,regTab,symTab,errorTab,size,lineNo,keyWords,i)
					lineNo+=1
				else :
					ERR.putError(errorTab,'',lineNo,4)
					lineNo+=1
		else:lineNo+=1

filename=input("Enter file name")
readFile(filename)
print("SYMBOL TABLE")
for j in symTab:
	print(j)
print("LITERAL TABLE")
for k in litTab:
	print(k)
print("ERROR TABLE")
for k,l in errorDict.items():
	print(k,l)
for k in symTab:
	if k[7]=="U":
		ERR.putError(errorTab,k[1],k[8],2)

if len(errorTab)!=0:
	for i in errorTab:
		print("line:%d %s '%s'"%(i[0],errorDict.get(i[2]),i[1]))
else:
	print("OBJECT CODE")
	P2.secondPass(filename,symTab,litTab,regTab)
