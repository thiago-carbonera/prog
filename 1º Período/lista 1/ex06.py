'''
6. Escreva um programa que lê o raio (r) de um círculo. O programa deve informar: o diâmetro, a
circunferência e a área do círculo. Considere:
a. pi (π) = 3.141593
b. Diâmetro = 2r
c. Circunferência = 2πr
d. Área = πr^2
'''

a= int(input("Raio: "))
pi=3.141593

print(f"Diâmetro = {2*a}")
print(f"Circunferência = {2* pi * a}")
print(f"Área = {pi * a**2}")
