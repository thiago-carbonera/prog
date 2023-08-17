'''
6. Escreva um programa que, dado um número inteiro positivo, imprime seus fatores primos.
Informe o numero:
> 132
2 x fator 2
1 x fator 3
1 x fator 11
'''
num = int(input("Valor desejado: "))
copy = num
div = 2
var = 0



while copy > 1: # while copy % div == 0:
    var = 0
    if copy % div == 0:
        copy //= div 
        var += 1
        print(f"{var} x fator de {div}")
    if copy % div != 0:
        div += 1  

