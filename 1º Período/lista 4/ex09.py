'''
9. Utilizando a função do exercício anterior, escreva uma função que imprime uma caixa, recebendo
como parâmetros:
a. Largura e altura da caixa (width e height);
b. O caractere de preenchimento da caixa (fill);
c. O caractere das bordas da caixa (edge).
Função: print_box(height: int, width: int, fill: str, edge: str)
Exemplo de uso:
print_box(5, 10, '#', 'o')
o--------o
|########|
|########|
|########|
o--------o
'''
def print_box(altura: int, largura: int, enchimento: str, borda: str):
    L = 1 #largura
    A = 1 #altura

    while A <= altura:
        if A == 1 or A == altura:
            while L <= largura:
                if L == 1:
                    print(f"\n{borda}", end = "")
                if L == largura:
                    print(f"{borda}", end = "")
                else:
                    print("-", end = "")
                
                L += 1
            L = 1
        else:
            while L <= largura:
                if L == 1:
                    print("\n|", end = "")
                if L == largura:
                    print("|", end = "")
                else:
                    print(enchimento, end = "")
                L += 1
            L = 1
        A += 1

def main():
    print_box(4, 10, "#", "+")
main()



