'''
3. Escreva um programa que, dado um número inteiro (positivo ou negativo) entre -99 e 99, o imprime
por extenso. Caso o número esteja fora desse intervalo, o programa deve informar um erro. Dica:
como o tamanho do número é conhecido (2 dígitos), você pode previamente desmontá-lo,
colocando cada dígito em variáveis separadas.
Informe o número: -57
> cinquenta e sete (negativo)
'''
a = int(input("Informe o número: "))
cont = 1
zero = 'zero'
um = 'um'
dois = 'dois'
tres = 'três'
quatro = 'quatro'
cinco = 'cinco'
seis = 'seis'
sete = 'sete'
oito = 'oito'
nove = 'nove'

print(f"Número {a} por extenso: ")
if a > 100 or a < -99:
    print("Erro!: digite apenas números entre -99 e 99")
else:
    if a < 0:
        print("Menos", end= " ")
        a *= -1
    dig1 = a // 10
    dig2 = a % 10
    while cont > 0:
        
        
        if dig1 == 1: # 10 - 19
            if dig2 == 0:
                print("Dez")
            if dig2 == 1:
                print("Onze")
            if dig2 == 2:
                print("Doze")
            if dig2 == 3:
                print("Treze")
            if dig2 == 4:
                print("Quatorze")
            if dig2 == 5:
                print("Quinze")
            if dig2 == 6:
                print("Dezesseis")
            if dig2 == 7:
                print("Dezessete")
            if dig2 == 8:
                print("Dezoito")
            if dig2 == 9:
                print("Dezenove")

        if dig1 == 2: # 20 - 29
            print("Vinte", end=" e ")
        if dig1 == 3: # 30 - 39
            print("Trinta", end=" e ")
        if dig1 == 4: 
            print("Quarenta", end=" e ")    
        if dig1 == 5: 
            print("Cinquenta", end=" e ") 
        if dig1 == 6: 
            print("Sessenta", end=" e ") 
        if dig1 == 7: 
            print("Setenta", end=" e ")
        if dig1 == 8: 
            print("Oitenta", end=" e ") 
        if dig1 == 9: 
            print("Noventa", end=" e ")

        if dig2 == 0: 
            print("\b\b ")     #conferir o print
        if dig2 == 1:
            print("Um")
        if dig2 == 2:
            print("Dois")
        if dig2 == 3:
            print("Três")
        if dig2 == 4:
            print("Quatro")
        if dig2 == 5:
            print("Cinco")
        if dig2 == 6:
            print("Seis")
        if dig2 == 7:
            print("Sete")
        if dig2 == 8:
            print("Oito")
        if dig2 == 9:
            print("Nove")

        if dig1 == 0 and dig2 == 0:
            print("Zero")
        cont -= 1
    









