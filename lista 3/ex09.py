'''
9. Escreva um programa que calcula a multiplicação de dois números inteiros utilizando somente o
operador aritmético de adição (+).
Exemplo:
Informe a x b: 5 7
5x7 = 35
'''
print("Mutiplicação: ")
valor1 = int(input("Valor desejado 1: "))
valor2 = int(input("Valor desejado 2: "))
a = 1
mult = 0

while a <= valor2:
    mult += valor1
    print(f"{valor1}",end=" + ")
    a += 1

print(f"\b\b= {mult}")
print(f"{valor1} * {valor2} = {mult}")
