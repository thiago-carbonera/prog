'''
11. Escreva uma função que imprime uma sequência de n números randômicos entre [left, right]
(inclusivos). Ao final, a função deve devolver a contagem de pares e primos. Considere 0 (zero)
como par. OBS: utilize a função is_prime(x) do exercício 3 para simplificar a verificação de número
primo.
Função: rand_report(n: int, left: int, right: int) -> tuple[int, int]
'''
import random

def rand_report(n: int, left: int, right: int):
    cont = 0
    num = 0
    par = 0
    div = 2
    primo = True
    numprim = 0
    
    while cont < n:
        num = random.randint(left, right)
        print(num, end = ", ")
        # verificador de par:
        if num % 2 == 0 or num == 0:
            par += 1
        
        #verificador de primo:
        for div in range (2, num // 2):    
            if num % div == 0:
                primo = False # não é primo
                break
        
        
        if num == 4:
            primo = False # 4 não é primo
        
        if primo == True:
            numprim += 1

        cont += 1
    print("\b\b ")
    print(f"Quantidade de pares: {par}")
    print(f"Quantidade de primos: {numprim}")





def main():
    rand_report(4, 0, 10)
main()



