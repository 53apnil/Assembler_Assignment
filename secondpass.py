opcodeTab={"mov r r":'89',"mov r i":'B8',"add r r":'01','add r i':'83C0','add r m':'81C0'}
regDict={'eax':'000','ecx':'001','edx':'010','ebx':'011','esp':'100','ebp':'101','esi':'110','edi':'111'}
size=0
i=0
def searchSize(string1,symTab):
	for k in range(0,len(symTab)):
		if string1==symTab[k][1]:
			if symTab[k][3]=="b":
				return [symTab[k][2],symTab[k][4]]
			else:
				return [symTab[k][2],symTab[k][6]]
def getAdd(string1,symTab):
	for k in range(0,len(symTab)):
		if string1==symTab[k][1]:
				return symTab[k][2]


def getOpcodeMov(string,j,regTab,symTab):
	global i
	global size
	str2=string.split(',')
	if str2[0] in regTab and str2[1] in regTab:
		i+=1
		opcode=opcodeTab.get("mov r r")
		op1=regDict.get(str2[0])
		op2=regDict.get(str2[1])
		str4='11'+op2[0:2]
		str5=op2[2:]+op1
		opcode=opcode+hex(int(str4,2))[2:]+hex(int(str5,2))[2:]
		print('{:<3} {:<8} {:<35} {:<20}'.format(i,hex(size)[2:].upper(),opcode.upper(),j))
		size+=2
		return
	elif str2[0] in regTab and str2[1].isdecimal():
		i+=1
		opcode=opcodeTab.get("mov r i")
		op1=regDict.get(str2[0])
		opcode=opcode[0]+str(hex((int(opcode[1])+int(op1,2)))[2:])
		opcode=opcode+hex(int(str2[1]))[2:]
		print('{:<3} {:<8} {:<35} {:<20}'.format(i,hex(size)[2:].upper(),opcode.upper(),j))
		size+=5
		return
	else:
		i+=1
		opcode=opcodeTab.get("mov r i")
		op1=regDict.get(str2[0])
		op2=getAdd(str2[1],symTab)
		opcode=opcode[0]+str(hex((int(opcode[1])+int(op1,2)))[2:])
		opcode=opcode+'['+str(op2)+']'
		print('{:<3} {:<8} {:<35} {:<20}'.format(i,hex(size)[2:].upper(),opcode.upper(),j))
		size+=5
		return

def getOpcodeAdd(string,j,regTab,symTab):
	global i
	global size
	str2=string.split(',')
	if str2[0] in regTab and str2[1] in regTab:
		i+=1
		opcode=opcodeTab.get("add r r")
		op1=regDict.get(str2[0])
		op2=regDict.get(str2[1])
		str4='11'+op2[0:2]
		str5=op2[2:]+op1
		opcode=opcode+hex(int(str4,2))[2:]+hex(int(str5,2))[2:]
		print('{:<3} {:<8} {:<35} {:<20}'.format(i,hex(size)[2:].upper(),opcode.upper(),j))
		size+=2
		return
	elif str2[0] in regTab and str2[1].isdecimal():
		i+=1
		opcode=opcodeTab.get("add r i")
		op1=regDict.get(str2[0])
		opcode=opcode[0:3]+str(hex((int(opcode[3])+int(op1,2)))[2:])
		opcode=opcode+hex(int(str2[1]))[2:]
		print('{:<3} {:<8} {:<35} {:<20}'.format(i,hex(size)[2:].upper(),opcode.upper(),j))
		size+=3
		return
	else:
		i+=1
		if str2[0]=="eax":
			opcode='05'
			op2=getAdd(str2[1],symTab)
			opcode=opcode+'['+str(op2)+']'
			print('{:<3} {:<8} {:<35} {:<20}'.format(i,hex(size)[2:].upper(),opcode.upper(),j))
			size+=5
			return
		else:
			opcode=opcodeTab.get("add r m")
			op1=regDict.get(str2[0])
			op2=getAdd(str2[1],symTab)
			opcode=opcode[0:3]+str(hex((int(opcode[3])+int(op1,2)))[2:])
			opcode=opcode+'['+str(op2)+']'
			print('{:<3} {:<8} {:<35} {:<20}'.format(i,hex(size)[2:].upper(),opcode.upper(),j))
			size+=6
			return
def secondPass(filename,symTab,litTab,regTab):
	fp=open(filename,"r")
	global i
	global size
	for j in fp:
		string=j.split()
		if "section .data" in j or "section .bss" in j or "section .text" in j or "global main" in j or "extern" in j:
			i+=1
			print('{:<3} {:<8} {:<35} {:<20}'.format(i,'','',j))
		elif len(string)==1:
			i+=1
			print('{:<3} {:<8} {:<35} {:<20}'.format(i,'','',j))
		elif string[1]=="dd" or string[1]=='db':
			i+=1
			sizeofVar,value=searchSize(string[0],symTab)
			print('{:<3} {:<8} {:<35} {:<20}'.format(i,sizeofVar.upper(),value,j))
		elif string[1]=="resb" or string[1]=='resd':
			i+=1
			sizeofVar,value=searchSize(string[0],symTab)
			print('{:<3} {:<8} {:35} {:<20}'.format(i,sizeofVar.upper(),"<res "+str(value)+">",j))
		elif string[0]=="mov":
			getOpcodeMov(string[1],j,regTab,symTab)
		elif "mov" in string[0]:
			getOpcodeMov(string[1],j,regTab,symTab)
		elif string[0]=="add":
			getOpcodeAdd(string[1],j,regTab,symTab)
		elif "add" in string[0]:
			getOpcodeAdd(string[1],j,regTab,symTab)
		elif "jmp" in string[0]:
			i+=1
			print('{:<3} {:<8} {:35} {:<20}'.format(i,hex(size)[2:].upper(),"EB00",j))
			size+=2
		else:continue			
