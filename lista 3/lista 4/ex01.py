'''
1. Escreva uma função que calcula e devolve o somatório de um número: .
𝑖=1
𝑛
∑ 𝑖
Função: def summation(n: int) -> int
OBS: Crie testes para todos os exercícios na função main():
'''
def summation (n: int):
    soma = 0
    while n > 0:
        soma += n
        n -= 1
    return soma

def main():
    print(summation(10))

main()




