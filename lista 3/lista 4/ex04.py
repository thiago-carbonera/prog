'''
4. Utilizando a função is_prime(x) do exercício anterior, escreva uma função que imprime os n
primeiros números primos.
Função: print_primes(n: int)
'''   
def is_prime(x: int):
    cont = True
    
    for div in range (2, x // 2):    
        if x % div == 0:
            cont = False
            x = 0
            break
    
    if x == 4:
        x = 0
        cont = False

    if cont == True:
        return x
    if cont == False:
        return x

    
def print_primes(n: int):
    cont1 = 0
    a = 2
    while cont1 < n:
        if is_prime(a) > 0:
            print(is_prime(a), end = ", ")
            a += 1
            cont1 += 1
        else:
            a += 1
    print("\b\b ")

def main():
    print_primes(8)
main()