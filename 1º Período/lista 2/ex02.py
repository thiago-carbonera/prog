'''
2. Escreva um programa que lê um número x do terminal e informa seu valor absoluto |x|, isto é:
a. |x| = x, se x > 0
b. |x| = -x, se x < 0
'''
a= int(input("Valor: "))

if a > 0:
    print(f"Valor em módulo = |{a}|")
else:
    if a < 0:
        print(f"Valor em módulo = |{-a}|")

