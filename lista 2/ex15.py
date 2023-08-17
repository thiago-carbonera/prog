'''
15. Escreva uma calculadora simples: faz a leitura de um operador char (+ - * / %), bem como, os
valores inteiros A e B. Então, o programa deve mostrar a expressão e o resultado (com dois dígitos
de precisão).
Exemplo:
[ CALCULADORA SIMPLEX ]
Operador> /
Número01> 20
Número02> 3
Expressão:
20 / 3 = 6.67
'''
oper= str(input("Operador: "))
n1= int(input("Número 1: ")) 
n2= int(input("Número 2: "))

print(" [Calculadora Simplex]")

print(f"Operador: {oper}")
print(f"Número 1: {n1}")
print(f"Número 2: {n2}")

print("<Expressão>: ")

if oper == "+" :
    print(f" {n1} + {n2} = {n1 + n2}")
if oper == "-" :
    print(f" {n1} - {n2} = {n1 - n2}")
if oper == "*" :
     print(f" {n1} * {n2} = {n1 * n2}")
if oper == "/" :
    print(f" {n1} / {n2} = {n1 / n2}")
if oper == "%" :
    print(f" {n1} % {n2} = {n1 % n2}")
               


