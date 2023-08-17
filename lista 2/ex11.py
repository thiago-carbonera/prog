'''
11. Escreva um programa que lê um caractere (string de 1 char) e informa se o mesmo é uma letra
maiúscula.
a. Considere como 'letra', todos os caracteres da língua portuguesa na tabela Unicode:
https://usefulwebtool.com/characters-portuguese
'''
a= int(input("Valor: "))


if a >= 65 and a <= 90:
    print("É uma letra maiúscula!")
else:
    print("Não é uma letra maiúscula!")
    
    

