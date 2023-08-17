'''
15. Escreva um programa que exibe o primeiro e o último dígitos de um número inteiro. Exemplo:
Informe o número: 12405
> Primeiro: 1
> Último : 5
'''
numero = int(input("Valor desejado: "))
resto = 0
resto1 = numero % 10


while numero != 0 or numero // 10 > 0:
    resto = numero % 10
    numero = numero // 10
    
print(f"Primeiro: {resto}")
print(f"Último: {resto1}")



