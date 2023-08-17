'''
1. Escreva um programa que faz a leitura de um valor N e imprime N linhas de texto exibindo o
número da linha corrente. Exemplo:
Informe o número de linhas: 10
Linha 1
Linha 2
Linha 3
…
Linha 10

'''
n = int(input("Valor de linhas desejado: "))
x = 1


while x <= n:
    print(f"linha {x}")
    x += 1





