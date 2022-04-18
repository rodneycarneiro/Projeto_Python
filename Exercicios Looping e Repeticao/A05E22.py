#Autor: Rodney Carneiro
#Data: 18/04/2022
#Objetivo: 
"""
Em uma eleição presidencial existem quatro candidatos. Os votos são informados através de
códigos. Os dados utilizados para a contagem dos votos obedecem à seguinte codificação:
- 1,2,3,4 = voto para os respectivos candidatos;
- 5 = voto nulo;
- 6 = voto em branco;
Elabore um algoritmo que leia o código do candidado em um voto. Calcule e escreva:
- total de votos para cada candidato;
- total de votos nulos;
- total de votos em branco;
Como finalizador do conjunto de votos, tem-se o valor 0.
"""
candidato1= 0
candidato2= 0
candidato3= 0
candidato4= 0
nulos = 0
brancos = 0
while True:
    print("==========================")
    print("| 1- Candidato 1         |")
    print("| 2- Candidato 2         |")
    print("| 3- Candidato 3         |")
    print("| 4- Candidato 4         |")
    print("| 5- Voto Nulo           |")
    print("| 6- Voto em Branco      |")
    print("==========================")
    print()
    voto=int(input("Digite seu Voto.: "))
    if (voto == 0):
        break
    elif (voto < 0) or (voto >6):
        print()
        print("Voto Incorreto.. Informe novamente")
        input()
    elif (voto > 0) and (voto <= 6):
        if (voto == 1):
            candidato1 = candidato1 + 1
        elif (voto == 2):
            candidato2 = candidato2 + 1
        if (voto == 3):
            candidato3 = candidato3 + 1
        elif (voto == 4):
            candidato4 = candidato4 + 1
        if (voto == 5):
            nulos = nulos + 1
        elif (voto == 6):
            brancos = brancos + 1

print("-="*30)
print("O resultado da Eleicao ficou da seguinte forma.: ")
print(f"  . Candidato1 teve um total de {candidato1} votos")
print(f"  . Candidato2 teve um total de {candidato2} votos")
print(f"  . Candidato3 teve um total de {candidato3} votos")
print(f"  . Candidato4 teve um total de {candidato4} votos")
print(f"  . Total de {nulos} votos Nulos")
print(f"  . Total de {candidato1} votos Brancos")
        