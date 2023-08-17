'''
12. Escreva um programa que faz a leitura de vários números inteiros (um a cada iteração do laço), até
que se digite zero. O programa deve imprimir o maior e o menor entre os números digitados.
Exemplo:
Informes os números:
> 5
> 10
> 3
> 7
> 0
Maior: 10
Menor: 3
'''
print("Valor desejado: ")
numero = int(input("> "))

maior = numero
menor = numero

while numero != 0:
    if maior < numero:
        maior = numero
    elif menor > numero:
        menor = numero
    numero = int(input("> "))
print(f'O maior número foi {maior} e o menor foi {menor}')


