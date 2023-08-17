'''
17. Escreva um programa que verifica se um número inteiro é um palíndromo, isto é, se representa o
mesmo valor quando invertido. Note que será necessário desmontar o número e remontá-lo
invertido. Para tanto, lembre-se de que utilizamos a base 10, o que torna possível “mover” um
número para esquerda multiplicando-o por 10.
Exemplos:
Informe o número: 24742
> 24742 = 24742
> Palíndromo!
Informe o número: 1752
> 1752 != 2571
> Não é palíndromo!
'''
numero = int(input("Valor desejado: "))
resto = 0
invertido = 0
c1 = 0
a = numero


while numero != 0 or numero // 10 > 0:
    resto = numero % 10
    invertido *= 10
    invertido += resto
    numero = numero // 10

print(f"{invertido}")
if a == invertido:
    print(f"O número é um palindromo")
else: 
    print(f"O número não é um palindromo")
