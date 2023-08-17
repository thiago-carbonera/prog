'''
7. Escreva um programa que lê dois números inteiros (a e b) e informa:
a. Resto (utilizado o operador %)
b. Resto (sem utilizar o operador %)
i. Dica: Faça a divisão “no papel” e observe quais outras operações podem ser
utilizadas para obter o resto.
'''

a= int(input("Valor 1: "))
b= int(input("valor 2: "))
rest= (a/b-(a/b)//1)*b

print(f"Resto normal = {a % b}")

print(f"Resto sem (%) = {rest}")

