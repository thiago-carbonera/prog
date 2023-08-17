'''
15. Escreva um programa que lê um número float (com parte decimal) e informa separadamente:
a. O número com 2 casas de precisão ("%.2f");
b. A parte inteira;
c. A parte decimal;
'''
a = float(input("Valor desejado: "))

print("%.2f" % a)
print(a // 1)
print(a // 1 - a)



