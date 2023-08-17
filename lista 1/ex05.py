'''
5. Escreva um programa que lê a largura e o comprimento de um retângulo. O programa deve
imprimir o perímetro e a área do retângulo. Considere:
a. Área = largura x comprimento
b. Perímetro = soma de todos os lados
'''

a= int(input("Largura: "))
b= int(input("Comprimento :"))

print(f"Área = {a * b}")
print(f"Perímetro = {2*a + 2*b}")

