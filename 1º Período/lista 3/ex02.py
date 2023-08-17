'''
2. Crie uma variação do programa anterior de forma que ele imprima as linhas em contagem
decrescente. Exemplo:
Informe o número de linhas: 10
Linha 10
Linha 9
Linha 8
…
Linha 1

'''
n = int(input("valor de linhas desejadas: "))
x = 1


while x <= n: 
    print(f"linha {n}")
    n -= 1

