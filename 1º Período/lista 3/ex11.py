'''
11. Escreva um programa que faz a leitura de vários números inteiros (um a cada iteração do laço), até
que se digite zero. O programa deve imprimir a soma e a média aritmética simples dos números
digitados.
Exemplo:
Informes os números:
> 5
> 10
> 3
> 7
> 0
Soma: 25
Media: 6.25
'''
print("Informe os números: ")
num = int(input("> "))
sum = 0
contador = 0

while num != 0:
    sum += num
    contador += 1
    num = int(input("> "))
    
    

print(f"\nSoma = {sum}")
print(f"Média simples = {sum / contador}")




