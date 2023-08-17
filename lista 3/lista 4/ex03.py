'''
3. Escreva uma função que verifica se um dado número é primo. A função deve devolver True, caso o
número seja primo, ou False, caso contrário.
Função: is_prime(x: int) -> bool
'''
def is_prime(x: int):
    div = 2
    cont = True

    if x == 4:
        cont = False
    for div in range (2, x // 2):    
        if x % div == 0:
            cont = False
            break
        
    
    print(f"O número {x} é primo?: {cont}")

def main():
    is_prime(2)
main()