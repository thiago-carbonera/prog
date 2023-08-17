'''
21. Em uma eleição existem quatro candidatos. Os votos são informados através de códigos. Os dados
utilizados para a contagem dos votos obedecem à seguinte codificação:
a. 1, 2, 3, 4: voto para os respectivos candidatos
b. 5 = voto nulo
c. 6 = votam em branco
Escreva um programa que faz a leitura de uma sequência de votos (até que zero seja digitado). Ao
final, o programa deve calcular e mostrar os totais de:
a. votos por candidato
b. votos nulos
c. Votos em branco
OBS: os votos em branco somam para o candidato que tiver mais votos (ao final)
'''
print("Votação da Pindamonhangaba!")
voto = int(input("Voto: "))
cand1 = 0
cand2 = 0
cand3 = 0
cand4 = 0
nulo5 = 0
branco6 = 0
votos_finais = 0

while voto != 0:
    if voto == 1:
        cand1 += 1
    if voto == 2:
        cand2 += 1
    if voto == 3:
        cand3 += 1
    if voto == 4:
        cand4 += 1
    if voto == 5:
        nulo5 += 1
    if voto == 6:
        branco6 += 1 
    voto = int(input("Voto: "))

if voto == 0:
    print(f"Votos candidato 1: {cand1}")
    print(f"Votos candidato 2: {cand2}")
    print(f"Votos candidato 3: {cand3}")
    print(f"Votos candidato 4: {cand4}")
    print(f"Votos nulos: {nulo5}")
    print(f"Votos brancos: {branco6}")

#votos finais totais (votos brancos vão para o vencedor)
if voto == 0:
    if cand1 > cand2 and cand1 > cand3 and cand1 > cand4:
        print(f"Vencedor é o candidato 1 com votos totais: {cand1 + branco6}")
    if cand2 > cand1 and cand2 > cand3 and cand2 > cand4:
        print(f"Vencedor é o candidato 2 com votos totais: {cand2 + branco6}")
    if cand3 > cand1 and cand3 > cand2 and cand3 > cand4:
        print(f"Vencedor é o candidato 3 com votos totais: {cand3 + branco6}")
    if cand4 > cand1 and cand4 > cand2 and cand4 > cand3:
        print(f"Vencedor é o candidato 4 com votos totais: {cand4 + branco6}")



