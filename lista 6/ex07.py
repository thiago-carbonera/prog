'''
7. Escreva uma função que recebe uma lista vet e um número value. A função deve retornar uma
outra lista, contendo os múltiplos de value que estão em vet.
def get_multiples(vet: list, value: int) -> list
'''
def get_multiples(vet: list, value: int):
    cont = 0
    mult = [0,0,0,0,0,0]
    var = 0

    print(f"Multiplos de {value} na lista:")
    while cont < len(vet):
        if vet[cont] % value == 0:
            mult[var] = vet[cont]
            var += 1
        
        if vet[cont] == 0:
            mult[var] = vet[cont]
            var += 1
            
        cont += 1
    
    print(mult)


def main():
    get_multiples([0,2,4,6,5,8], 2)
main()    