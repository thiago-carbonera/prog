'''
2. Escreva uma função que recebe uma lista vet e imprime apenas os valores pares.
def print_even(vet: list)
'''

def print_even(vet: list):
    cont = 0
    tam = 0
    
    while cont < len(vet):
        if vet[tam] % 2 == 0:
            print(vet[tam])
        cont += 1
        tam += 1

def main():
    print_even([1,2,6,5,4])
main()







