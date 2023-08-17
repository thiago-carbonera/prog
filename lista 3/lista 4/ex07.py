'''
7. Escreva uma função que imprime N números inteiros aleatórios. A função receberá como
parâmetro a quantidade de números (n) e os limites para sorteio (min e max). Os números devem
ser randomizados entre [min, max]. Utilize a semente 1 antes de gerar os números, isto é,
random.seed(1).
OBS: Será necessário utilizar a função random.randint() do módulo random. Para tanto, importe o
módulo random com import random.
Função: print_random(n: int, min: int, max: int)
'''
import random

def print_random(n: int, min: int, max: int):
    cont = 0
    while cont < n:
        print(random.randint(min, max), end = ", ")
        cont += 1
    print("\b\b ")

def main():
    print_random(4, 1, 10)
main()





