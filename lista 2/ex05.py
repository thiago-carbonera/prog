'''
5. Escreva um programa que lê dois números naturais e informa o maior. O programa também deve
informar se os números são iguais. Caso o utilizador entre com números negativos, o programa
deve informar um erro e não realizar as demais verificações.
'''

a = int(input("Valor 1: "))
b = int(input("valor 2: "))

if a < 0:
    print(f"insira apenas números positivos!")
else:
    if b < 0:
        print(f"insira apenas números positivos!")

    if a > b and a >= 0:
        print(f"{a} é maior que {b}!")
    else:
        if a < b and b >= 0:
            print(f"{b} é maior que {a}!")

    if a == b :
        print("Os números escolhidos são iguais!")


