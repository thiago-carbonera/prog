print("Calculadora simples")
print("Operador: + , - , * , / , **,  % , //")
a = int(input("Número 1: "))
op = input("Operador: ")
b = int(input("Número 2: "))

res = 0

if op == '+':    # Soma
    res = a + b
if op == '-':    # Subtração
    res = a - b
if op == '*':    # Multiplicação
    res = a * b
if op == '/':    # Divisão float
    res = a / b
if op == '//':   # Divisão inteiro
    res = a // b
if op == '%':    # Resto de divisão
    res = a % b
if op == '**':   # Exponenciação
    res = a ** b
    
print(f"{a} {op} {b} = {res}")