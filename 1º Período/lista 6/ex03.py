'''
3. Escreva uma função que recebe uma lista vet contendo números inteiros. A função deve modificar
a lista, invertendo o sinal dos números negativos, passando-os para positivo.
def set_positive(vet: list)
Ex: Entrada:[1, -5, 67, -45, -1, -1, 0, 48] → Saída:[1, 5, 67, 45, 1, 1, 0, 48]
'''
def set_positive(vet: list):
    cont = 0
    pos = 0

    while cont < len(vet):
        if vet[cont] < 0:
            pos = vet[cont]
            print(pos * -1, end = ", ")
        else:
            print(vet[cont], end = ", ")
        cont += 1
    print("\b\b ")

def main():
    set_positive([1,-1,-4,7,8,-9])
main()