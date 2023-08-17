'''
14. Escreva um programa que lê um número float (com parte decimal) e informa separadamente:
a. O número com 2 casas de precisão ("%.2f");
b. A parte inteira;
c. A parte decimal;
'''

a= float(input("Número: "))
b= a//1
c= a - b

print(" 2 casas: %.2f" % (a)) 
print(f" Inteiro: {b}") 
print(f" Parte decimal: {c}")



