'''
6. Escreva um programa que lê um inteiro representando um ano e verifica se o mesmo é bissexto.
Para um ano ser bissexto (leap year), ele precisa:
a. Ser divisível por 4 e não divisível por 100, OU, ser divisível por 400.
'''

a= int(input("Ano desejado: "))

if a % 4 == 0:
    print(f"O ano {a} é um ano bissexto!")
else:
    print(f"O ano {a} não é um ano bissexto!")


