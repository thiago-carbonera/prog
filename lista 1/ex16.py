'''
16. Escreva um programa que lê um número de dias e converte em: anos + semanas + dias.
a. Considere:
i. Ano = 365 dias
ii. Semana = 7 dias
Exemplo:
Dias: 427 = 1 ano(s), 8 semana(s) e 6 dia(s)
'''
a= int(input("Dias: "))
b= a / 365
c=  b // 1 
d= a % 365
e= d / 7
f= e // 1
g=  d % 7


print(f"Anos: {c}")
print(f"Semanas: {f}")
print(f"Dias: {g}")





