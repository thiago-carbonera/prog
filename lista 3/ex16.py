'''
16. Escreva um programa que exibe a frequência de cada dígito em um número inteiro.
Informe o número: 1251055
> Frequência de 0: 1
> Frequência de 1: 2
> Frequência de 2: 1
> Frequência de 3: 0
> Frequência de 4: 0
> Frequência de 5: 3
> Frequência de 6: 0
> Frequência de 7: 0
> Frequência de 8: 0
> Frequência de 9: 0
'''
numero = int(input("Valor desejado: "))
resto = 0
c0, c1, c2, c3, c4, c5, c6, c7, c8, c9 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
a = 1


while numero != 0 or numero // 10 > 0:
    resto = numero % 10
    numero = numero // 10
    if resto == 0:
        c0 += 1
    if resto == 1:
        c1 += 1
    if resto == 2:
        c2 += 1
    if resto == 3:
        c3 += 1
    if resto == 4:
        c4 += 1
    if resto == 5:
        c5 += 1
    if resto == 6:
        c6 += 1
    if resto == 7:
        c7 += 1
    if resto == 8:
        c8 += 1
    if resto == 9:
        c9 += 1

print(f"Frequência de 0 = {c0}")
print(f"Frequência de 1 = {c1}")
print(f"Frequência de 2 = {c2}")
print(f"Frequência de 3 = {c3}")
print(f"Frequência de 4 = {c4}")
print(f"Frequência de 5 = {c5}")
print(f"Frequência de 6 = {c6}")
print(f"Frequência de 7 = {c7}")
print(f"Frequência de 8 = {c8}")
print(f"Frequência de 9 = {c9}")