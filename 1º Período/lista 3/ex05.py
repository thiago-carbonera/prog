'''
5. Escreva um programa que imprime todas as letras do alfabeto (minúscula e maiúscula), segundo o
exemplo:
LETRAS DO ALFABETO:
a | A
b | B
c | C
...

'''

print("Letras do alfabeto: ")
for i in range (0,26):
    print(f"{chr(i + 65)} | {chr(i + 97)}")


