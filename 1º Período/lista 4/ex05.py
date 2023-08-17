'''
5. Escreva uma função que calcula e devolve a soma dos fatoriais até um dado número, . Você
𝑖=1
𝑛
∑ 𝑖!
pode escrever uma solução que utiliza 2 laços aninhados (laço dentro de laço).
Função: factorial_sum(n: int) -> int
Exemplo de uso:
print(factorial_sum(5)) # deve calcular 1! + 2! + 3! + 4! + 5! = 153
'''
def factorial_sum(n: int):
    cont = 1

    while n > 0:
        cont *= n
        n -= 1
    print(cont)


def main():
    factorial_sum(5)
main()    


