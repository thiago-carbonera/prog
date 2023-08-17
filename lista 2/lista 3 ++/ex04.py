'''
4. Escreva um programa que, dado um número inteiro (positivo ou negativo) entre -999 e 999, o
imprime por extenso. Caso o número esteja fora desse intervalo, o programa deve informar um
erro.
Informe o número: 572
> quinhentos e setenta e dois (positivo)
'''
a = int(input("Informe o número: "))
var = 0
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
if a > 999 or a < -999:
    print("Erro!: digite apenas números entre -99 e 99")
else:
    if a < 0:
        print("Menos", end= " ")
        a *= -1
    dig1 = a // 100
    var = a // 10
    dig2 = var % 10
    dig3 = a % 10
    while cont > 0:
        
        if dig1 == 1:
            print("Cento", end=" e ")
        if dig1 == 2:
            print("Duzentos", end=" e ")
        if dig1 == 3:
            print("Trezentos", end=" e ")
        if dig1 == 4: 
            print("Quatrocentos", end=" e ")    
        if dig1 == 5: 
            print("Quinhentos", end=" e ") 
        if dig1 == 6: 
            print("Seissentos", end=" e ") 
        if dig1 == 7: 
            print("Setecentos", end=" e ")
        if dig1 == 8: 
            print("Oitocentos", end=" e ") 
        if dig1 == 9: 
            print("Novecentos", end=" e ")





        if dig2 == 1: # 10 - 19
            if dig3 == 0:
                print("Dez")
            if dig3 == 1:
                print("Onze")
            if dig3 == 2:
                print("Doze")
            if dig3 == 3:
                print("Treze")
            if dig3 == 4:
                print("Quatorze")
            if dig3 == 5:
                print("Quinze")
            if dig3 == 6:
                print("Dezesseis")
            if dig3 == 7:
                print("Dezessete")
            if dig3 == 8:
                print("Dezoito")
            if dig3 == 9:
                print("Dezenove")

        if dig2 == 2: # 20 - 29
            print("Vinte", end=" e ")
        if dig2 == 3: # 30 - 39
            print("Trinta", end=" e ")
        if dig2 == 4: 
            print("Quarenta", end=" e ")    
        if dig2 == 5: 
            print("Cinquenta", end=" e ") 
        if dig2 == 6: 
            print("Sessenta", end=" e ") 
        if dig2 == 7: 
            print("Setenta", end=" e ")
        if dig2 == 8: 
            print("Oitenta", end=" e ") 
        if dig2 == 9: 
            print("Noventa", end=" e ")

        if dig3 == 0: 
            print("\b\b ")     
        if dig3 == 1:
            print("Um")
        if dig3 == 2:
            print("Dois")
        if dig3 == 3:
            print("Três")
        if dig3 == 4:
            print("Quatro")
        if dig3 == 5:
            print("Cinco")
        if dig3 == 6:
            print("Seis")
        if dig3 == 7:
            print("Sete")
        if dig3 == 8:
            print("Oito")
        if dig3 == 9:
            print("Nove")

        if dig1 == 0 and dig2 == 0 and dig3 == 0:
            print("Zero")
        cont -= 1
