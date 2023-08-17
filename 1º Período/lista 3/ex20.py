'''
20. A série de Fibonacci é 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Os dois primeiros termos são iguais a 1 e, a
partir do terceiro, o termo é dado pela soma dos dois termos anteriores. Dado um número n≥3,
exiba o n-ésimo termo da série de Fibonacci.
'''
termo = int(input("Termo desejado (n >= 3): "))
t1 = 1
t2 = 1
som = 0
i = 2
while i < termo:
   som = t1 + t2
   t1 = t2
   t2 = som
   i += 1
print(f"O termo {termo + 2} na série de Fibonacci é: {som}")