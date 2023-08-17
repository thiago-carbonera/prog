'''
8. Escreva uma função que recebe uma lista vet e retorna uma outra lista, com os primos em vet.
def get_primes(vet: list) -> list
'''
def get_primes(vet: list,): #voltar números primos
    cont = 0
    lista = [0,0,0,0,0,0]
    var = 0
    primo = True

    print("Números primos na lista:")
    while cont < len(vet):
        primo = True
        for div in range (2, vet[cont // 2]):
            
            if vet[cont] % div == 0: #não é primo
                primo = False
                break
            
        if vet[cont] == 4:
            primo = False

        if vet[cont] == 0:
            primo = False

        if vet[cont] == 2 or vet[cont] == 3:
            primo = True

        if primo == True:
            lista[var] = vet[cont]
            var += 1
           
        cont += 1
    
    print(lista)


def main():
    get_primes([0,2,4,3,5,11])
main()    





