#Autor: Rodney Carneiro
#Data: 18/04/2022
#Objetivo: 
"""
Escrever um algoritmo que leia 5 conjuntos de 2 valores, o primeiro representando o número de
um aluno, e o segundo representando a sua altura em centímetros.
Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e do mais baixo,
junto com suas alturas.
"""


maior = 0
menor = 999

for i in range(5):
    numero = int(input("Digite o número {} do aluno: ".format(i + 1)))
    nome = str(input("Digite o nome do aluno: "))
    altura = float(input("Digite a altura do aluno: "))

    if altura > maior :
        maior = altura
        num_maior = numero
        nome_maior = nome

    if altura < menor :
        menor = altura
        num_menor = numero
        nome_menor = nome

print("Aluno que tem a maior altura: ")
print("Número: {}".format(num_maior))
print("Nome: {}".format(nome_maior))
print("Altura: {}".format(maior))

print("Aluno que tem a menor altura: ")
print("Número: {}".format(num_menor))
print("Nome: {}".format(nome_menor))
print("Altura: {}".format(menor))
