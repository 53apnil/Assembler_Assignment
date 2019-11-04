section .data
    msg db "This is a String",10,0
    data db "This is data",10,0 
    a dd 10,20
    b dd 20,40
    c dd 20 
section .bss
    d resd 1
    e resb 2
section .text
main:
    mov eax,ebx
    mov ebx,ecx
    mov ecx,edx
    mov ecx,b
    mov edx,a
    jmp pqr
    mov eax,10
    mov ecx,30
pqr:mov edx,40
    add eax,ecx
    add ecx,edx
    add eax,20
    add ecx,50
    add edx,70
    add ebx,90
    add eax,a
    add ecx,b
    add edx,c
    add ebx,data
