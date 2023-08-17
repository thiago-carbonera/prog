'''
10. Escreva uma função que imprime uma sequência de n números randômicos entre [left, right]
(inclusivos). Ao final, a função deve devolver o maior e o menor números sorteados.
Função: print_random2(n: int, left: int, right: int) -> tuple[int, int]
'''
import random

def  print_random2(n: int, left: int, right: int):
    cont = 0
    num = 0
    min = right
    max = left 
    
    while cont < n:
        num = random.randint(left, right)
        print(num, end = ", ")

        if num > max: # 4 > 0  : max=num
            max = num
        if num < min: # min = num
            min = num

        cont += 1
    print("\b\b ")
    print(f"O maior número é: {max}")
    print(f"O menor número é: {min}")

def main():
    print_random2(3, 1, 50)
main()


