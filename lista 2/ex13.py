'''
13. Escreva um programa que lê um caractere da entrada. Se não for letra, informa. Se for letra,
verifica se é maiúscula (e passa para maiúscula se necessário). Ao final, deve informar a letra
digitada em maiúsculo.
'''
a = int(input("Valor desejado: "))

if a >= 0 and a < 65:
    print(f"{a} não é uma letra!")
else:
    if (a >= 65 and a <= 90):
        print(f"{a} é uma letra maiúscula: {chr(a)}")
    if (a >= 97 and a <= 122):
        print(f"{a} é uma letra: {chr (a - 32)}")


