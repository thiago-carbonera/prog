'''
3. Escreva um programa que imprime a tabuada de um número informado. Exemplo:
Informe o número: 7
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
…
7 x 10 = 70

'''
n = int(input("valor desejado: "))
x = 1

print(f"Tabuada do número {n} \n")
while x <= 10:
    print(f"{n} x {x} = {n * x}")
    x += 1



