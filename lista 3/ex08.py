'''
8. Escreva um programa que calcula o fatorial de um número natural. Por definição: 0! = 1 e 1! = 1
Exemplo:
Informe o número: 5
5! = 1 x 2 x 3 x 4 x 5 = 120

'''
numero = int(input("Número para fatorial: "))
a = 1
soma = 1

print(f"{numero}! :")
while a <= numero:
    soma *= a
    print(f"{a}",end=' * ') 
    if a == numero:
        print(f"\b\b= {soma}")
    a += 1
