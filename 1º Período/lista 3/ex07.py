'''
7. Escreva um programa que calcula o somatório de um número natural X fornecido pelo teclado.
Exemplo:
Informe o número: 5
1 + 2 + 3 + 4 + 5 = 15
'''
numero = int(input("Número para o somatorio: "))
a= 1
soma = 0

while a <= numero:
    soma += a
    print(f"{a}",end=' + ') 
    if a == numero:
        print(f"\b\b= {soma}")
    a += 1