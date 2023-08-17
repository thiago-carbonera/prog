'''
10. Escreva um programa que lê um número de 5 dígitos e imprime cada dígito separado. Para
desmontar um número, podemos utilizar a notação posicional, isto é, o valor de cada dígito em
relação a uma potência de 10. Observe o exemplo:
O processo ocorre como uma repetição de dois passos:
a. Calcular o resto da divisão do número por 10 para obtermos o dígito da unidade.
b. Atualizar o número, dividindo-o por 10. Isso fará o número perder um dígito.
n = 23491
'''
a= int(input("Valor: "))
n1= a % 10
b= a // 10
n2= b % 10
c= b // 10
n3= c % 10
d= c // 10
n4= d % 10
e= d // 10
n5= e % 10

print(f"número em digitos separados: {n5},{n4},{n3},{n2},{n1}")

