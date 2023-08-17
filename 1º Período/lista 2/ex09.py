'''
9. Escreva um programa que lê três números e os escreve em ordem crescente.
'''
a= int(input("Valor 1: "))
b= int(input("Valor 2: "))
c= int(input("Valor 3: "))

if b > c and a > b:
    print(f"ordem crescente: {a}, {b}, {c}")
if c > b and a > c:
    print(f"ordem crescente: {a}, {c}, {b}")
if a > c and b > a:
    print(f"ordem crescente: {b}, {a}, {c}")
if c > a and b > c:
    print(f"ordem crescente: {b}, {c}, {a}")
if a > b and c > a:
    print(f"ordem crescente: {c}, {a}, {b}")
if b > a and c > b:
    print(f"ordem crescente: {c}, {b}, {a}")

