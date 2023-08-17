'''
5. Escreva um programa que, dado um número inteiro positivo, verifica se o mesmo é um Número
Perfeito. Um número perfeito é igual à soma de seus divisores positivos. Exemplo: 6 = 1 + 2 + 3,
Informe o numero: 6
Divisores de 6: 1 + 2 + 3 = 6
Numero perfeito? Sim
'''
num = int(input("Informe o número: "))
cont = 0
div = 1
perf = 0
verif = False

while div <= num // 2:
    if num % div == 0:
        perf += div
    div += 1

if perf == num:
    verif = True

print(f"O número {num} é um número perfeito: {verif}")







