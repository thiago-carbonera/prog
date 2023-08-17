'''
7. Escreva um programa que faz a leitura de três notas escolares float - n1, n2 e n3 - no intervalo
[0..10]. Após, deve calcular e informar a média aritmética simples das três notas, bem como, o
conceito que o aluno obteve com base na média, segundo estes critérios:
a. Conceito A, se média no intervalo [8,5..10]
b. Conceito B, se média no intervalo [7,0..8,5[
c. Conceito C, se média no intervalo [5,5..7,0[
d. Conceito F, se média no intervalo [0..5,5[
'''
n1= float(input("Nota 1: "))
n2= float(input("Nota 2: "))
n3= float(input("Nota 3: "))
a= (n1 + n2 + n3) / 3

print(f"Média: {a}")

if (n1 >= 0 and n1 <=10) and (n2 >= 0 and n2 <= 10) and (n3 >= 0 and n3 <= 10):
    if 8.5 <= a <= 10:
        print(f"Aluno obteve conceito A!")
    if 7.0 <= a < 8.5:
        print(f"Aluno obteve conceito B!")
    if 5.5 <= a < 7.0:
        print(f"Aluno obteve conceito C!")
    if 0 <= a < 5.5:
        print(f"Aluno obteve conceito F!")

