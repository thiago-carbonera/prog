'''
12. Escreva um programa que lê três números inteiros (a, b e c) e informa:
a. A média aritmética simples dos três valores.
b. A média ponderada dos três valores, considerando como pesos 10% (a), 50% (b) e 40% (c)
'''
a= int(input("Número 1: "))
b= int(input("Número 2: "))
c= int(input("Número 3: "))

print(f"Média aritmética: {(a + b + c) / 3}")
print(f"Média ponderada: {(a * 0.1 + b * 0.5 + c * 0.4) / (0.1 + 0.5 + 0.4)}")
