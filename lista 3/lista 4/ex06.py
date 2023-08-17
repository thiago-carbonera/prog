'''
6. Escreva uma nova versão da função do exercício anterior, agora utilizando apenas um único laço
para realizar a operação solicitada na função. Dica: observe a representação dos cálculos.
Função: factorial_sum2(n: int) -> int
Exemplo de uso:
print(factorial_sum2(5))
1! + 2! + 3! + 4! + 5! = 153, é o mesmo que:
1! = 1 = 1 +
2! = 1 x 2 = 2 +
3! = 1 x 2 x 3 = 6 +
4! = 1 x 2 x 3 x 4 = 24 +
5! = 1 x 2 x 3 x 4 x 5= 120
                        153
'''
def factorial_sum(n: int):
    cont = 1
    print(f"{n}! :", end =" ")

    while n > 0:
        print(f"{n}", end = " x ")
        cont *= n
        n -= 1
        
    print(f"\b\b= {cont}")



def main():
    factorial_sum(5)
main()    