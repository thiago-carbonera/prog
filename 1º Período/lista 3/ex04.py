'''
4. Escreva um programa que imprime os N primeiros ímpares. Exemplo:
Quantos ímpares deseja?: 11
1 3 5 7 9 11 13 15 17 19 21
'''
n = int(input("valor desejado de números ímpares: "))

for i in range (0, n*2):
    if (i % 2 == 1) or (i == 1):
        print(f"{i}")



