'''
5. Escreva uma função que recebe uma lista vet, bem como, um elemento elem a ser procurado. A
função deve retornar a posição (índice) do elemento ou None caso ele não esteja no vetor.
def find(vet: list, elem: int)
'''
def find(vet: list, elem: int):
    cont = 0
    var = False 

    while cont < len(vet):
        if vet[cont] == elem: #retornar a posição
            print(f"O elemento está na lista!")
            print(f"Na posição: {cont}")
            var = True
        
        cont += 1
    if var == False:
        print(f"O elemento {elem} não está na lista!")

def main():
    find([1,2,3,4,6,8,5], 6 )
main()    