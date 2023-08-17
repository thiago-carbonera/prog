'''
19. Escreva um programa que verifica se um número inteiro é primo, isto é, possui divisão exata
somente pelo próprio número ou por 1. Exemplo:
Informe o número: 67
Resposta: primo
'''
numero = int(input("Valor desejado: "))
c1 = 2

while numero % c1 != 0:
    c1 += 1
    
if c1 == numero:
    print(f"O número {numero} é primo!")
if c1 != numero:
    print(f"O número {numero} não é primo!")


