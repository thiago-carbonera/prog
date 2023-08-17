'''
8. Escreva um programa que lê quatro números e informa o maior digitado.
'''
a= int(input("Valor 1: "))
b= int(input("Valor 2: "))
c= int(input("Valor 3: "))
d= int(input("Valor 4: "))

if a > b and a > c and a > d:
    print(f"{a} é o maior número selecionado!")
if b > a and b > c and b > d:
    print(f"{b} é o maior número selecionado!")
if c > a and c > b and c > d:
    print(f"{c} é o maior número selecionado!")
else:
    print(f"{d} é o maior número selecionado!")


