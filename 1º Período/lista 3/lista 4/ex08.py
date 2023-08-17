'''
8. Escreva uma função que imprime uma linha com duas “pontas”. A função receberá como
parâmetros: a largura da linha (n), o caractere de preenchimento da linha (fill) e o caractere das
pontas da linha (edge).
Função: print_line(n: int, fill: str, edge: str)
Exemplo de uso:
print_line(10, '-', '+') # Saída: +--------+
'''
def print_line(n: int, fill: str, edge: str):
    linha = 1
    while linha <= n:
        if linha == 1 or linha == n:
            #pontas
            print(edge, end="")
        else:
            #meio
            print(fill, end="")
        linha += 1
     

def main():
    print_line(10, "-", "+")
main()    

        
