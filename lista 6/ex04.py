'''
4. Escreva uma função que recebe uma lista vet e devolve a média aritmética simples dos elementos.
def list_sum(vet: list) -> float
Ex: Entrada: [1, 23, 4, 8, 41, 7, 3] → Saída: 12
'''
def list_sum(vet: list):
    cont = 0
    som = 0

    while cont < len(vet):
        som += vet[cont]
        cont += 1
    print(f"Média aritmética simples: {som / len(vet)}")
    print(f"Média aritmética simples parte inteira: {som // len(vet)}")



def main():
    list_sum([1,23,4,8,41,7,3])
main()



