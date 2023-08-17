'''
1. Escreva uma função que recebe uma lista vet a imprime em ordem reversa. Não é permitido o uso
de list.reverse().
def print_reverse(vet: list)
'''
def print_reverse(vet: list):
    tam = len(vet) - 1
    while tam >= 0:
        print(f"{vet[tam]}", end = ", ")
        tam -= 1
    print("\b\b ")





def main():
    print_reverse([1,2,3,4])
main()



