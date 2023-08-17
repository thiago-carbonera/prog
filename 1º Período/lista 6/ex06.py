'''
6. Escreva uma função que recebe uma lista vet ordenado crescentemente, bem como, um elemento
elem a ser procurado. A função deve retornar a posição (índice) do elemento ou None caso ele
não esteja na lista. OBS: Tente usar o fato da lista estar ordenada para criar uma solução
melhor que a anterior
def find(vet: list, elem: int)
'''
def find(vet: list, elem: int):
    cont = 0
    ver = False
    meio = len(vet) // 2
    
    if elem < vet[meio]: #o elem é menor q o meio da lista
        while cont < len(vet) // 2:
            if vet[cont] == elem:
                print(f"O elemento está na posição: {cont}")
                ver = True
            cont += 1    

    if elem > vet[meio]: #o elem é maior q o meio da lista
        cont = len(vet) // 2
        while cont < len(vet):
            if vet[cont] == elem:
                print(f"O elemento está na posição: {cont}")
                ver = True
            cont += 1 

    if elem == vet[meio]:
        print(f"O elemento está na posição: {len(vet) // 2}")
        ver = True

    if ver == False:
        print(f"O elemento não está na lista!")
        
def main():
    find([1,1,1,2,8,9], 2)
main()