Run the assembler.py first and then enter assembly file name 
and then it will show the output.



Enter file name file.asm
It will generate the the following output
SYMBOL TABLE
[1, 'msg', '0', 'd', 1, 18, '54686973206973206120537472696E67A0', 'D', 2]
[2, 'data', '12', 'd', 1, 14, '546869732069732064617461A0', 'D', 3]
[3, 'a', '20', 'd', 4, 2, 'A14', 'D', 4]
[4, 'b', '28', 'd', 4, 2, '1428', 'D', 5]
[5, 'c', '30', 'd', 4, 1, '14', 'D', 6]
[6, 'd', '0', 'b', 4, '', '', 'D', 8]
[7, 'e', '4', 'b', 2, '', '', 'D', 9]
[8, 'main', 0, 't', '', '', '', 'D', 11]
[9, 'pqr', 0, 't', '', '', '', 'D', 17]
LITERAL TABLE
[1, '10', 'A']
[2, '30', '1E']
[3, '40', '28']
[4, '20', '14']
[5, '50', '32']
[6, '70', '46']
[7, '90', '5A']
ERROR TABLE
1 error:symbol redefined
2 error:symbol undefined
3 error:keyword is used as an identifier
4 error:invalid use of opcode and operands
OBJECT CODE
1                                                section .data
      
2   0        54686973206973206120537472696E67A0      msg db "This is a String",10,0

3   12       546869732069732064617461A0              data db "This is data",10,0 

4   20       A14                                     a dd 10,20
     
5   28       1428                                    b dd 20,40
     
6   30       14                                      c dd 20 
       
7                                                section .bss
       
8   0        <res 4>                                 d resd 1
       
9   4        <res 2>                                 e resb 2
       
10                                               section .text
      
11                                               main:
              
12  0        89D8                                    mov eax,ebx
    
13  2        89CB                                    mov ebx,ecx
    
14  4        89D1                                    mov ecx,edx
    
15  6        B9[28]                                  mov ecx,b
      
16  B        BA[20]                                  mov edx,a
      
17  10       EB00                                    jmp pqr
        
18  12       B8A                                     mov eax,10
     
19  17       B91E                                    mov ecx,30
     
20  1C       BA28                                pqr:mov edx,40
     
21  21       01C8                                    add eax,ecx
    
22  23       01D1                                    add ecx,edx
    
23  25       83C014                                  add eax,20
     
24  28       83C132                                  add ecx,50
     
25  2B       83C246                                  add edx,70
     
26  2E       83C35A                                  add ebx,90
     
27  31       05[20]                                  add eax,a
      
28  36       81C1[28]                                add ecx,b
      
29  3C       81C2[30]                                add edx,c
      
30  42       81C3[12]                                add ebx,data
   

