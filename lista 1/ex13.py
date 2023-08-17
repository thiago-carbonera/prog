'''
13. Modifique o programa anterior, letra (b), para que seja possível informar os 3 pesos, além dos 3
valores.
'''
a= int(input("Número 1: "))
b= int(input("Número 2: "))
c= int(input("Número 3: "))
p1= float(input("Peso 1: "))
p2= float(input("Peso 2: "))
p3= float(input("Peso 3: "))

print(f"Média ponderada: {(a * p1 + b * p2 + c * p3) / p1 + p2 + p3}")


