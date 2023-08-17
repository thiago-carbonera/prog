'''
18. O quadrado de um número natural n é dado pela soma dos n primeiros números ímpares
consecutivos. Por exemplo, 1²=1, 2²=1+3, 3²=1+3+5, 4²=1+3+5+7, etc. Dado um número n, calcule
seu quadrado usando a soma de ímpares.
'''
numero = int(input("Valor desejadp: "))
c1 = 1
c3 = 1
n1 = numero ** 2

while n1 > c3:
    c1 += 2
    c3 += c1

print(f"O quadrado do número {numero} = {c3}")




