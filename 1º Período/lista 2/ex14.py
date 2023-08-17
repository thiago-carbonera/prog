'''
14. Escreva um programa que lê um caractere e informa:
a. Se é letra e, neste caso, também informa se é vogal ou consoante;
b. Se é número;
c. Se é símbolo (ASCII 33 ao 126, exceto números e símbolos).
'''
a= str(input("caractere desejado: "))
b= ord(a)

if (b >= 65 and b <= 90) or (b >= 97 and b <= 122):
    if (b == 65) or (b == 69) or (b == 73) or (b == 79) or (b == 85) or (b == 97) or (b == 101) or (b == 105) or (b == 79 + 32) or (b == 85 + 32):
        print(f"{a} é uma vogal!")
    else:
        print(f"{a} é uma consoante!")

elif (b >= 48 and b <= 57):
    print(f"{a} é um número!")

elif (b >= 33 and b <= 126):
    print(f"{a} é um símbolo!")




