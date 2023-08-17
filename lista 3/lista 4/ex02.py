'''
2. Utilizando a função summation(n) do exercício anterior, escreva uma função que devolve o
produto (multiplicação) dos somatórios de dois números.
Função: def summation_product(a: int, b: int) -> int
'''
def summation (num: int):
    soma = 0
    while num > 0:
        soma += num
        num -= 1
    return soma

def summation_product(a:int , b:int):
    return summation(a) * summation(b)
    
def main():
    print(summation_product(5, 2))

main()