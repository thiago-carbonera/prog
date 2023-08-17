'''
1. Escreva um programa que, dado um número inteiro (positivo ou negativo), troca o último dígito pelo
primeiro. OBS: não basta imprimir o número dessa forma, é preciso inverter o número em uma
variável int.
Informe o número: -2567
> -7562
'''

num = int(input("Valor desejado: "))
num1 = num
cont = 0
prim = 0
fim = 0
var = num
fim2= 0

ult = num % 10   # ultimo digito
while 10 < num1:  # primeiro digito
    prim = num1 // 10
    num1 = prim

while var // 10:
    var //= 10
    cont += 1

fim = num - num1 * 10 ** cont
fim += ult * 10 ** cont
fim -= ult
fim += num1

print(fim)









