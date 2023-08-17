'''
4. Escreva um programa que lê um número de 0 a 9 e o imprime por extenso. O programa deve
validar a entrada (0 <= x <= 9) e informar erro, caso ocorra.
'''

a= int(input("Valor de 0 a 9: "))

if a == 0:
    print("Valor: zero")
if a == 1:
    print("Valor: um")
if a == 2:
    print("Valor: dois")
if a == 3:
    print("Valor: três")
if a == 4:
    print("Valor: quatro")
if a == 5:
    print("valor: cinco")
if a == 6:
    print("Valor: seis")
if a == 7:
    print("Valor: sete")
if a == 8:
    print("Valor: oito")
if a == 9:
    print("Valor: nove")
if a > 9:
    print("insira um número de 0 a 9")

