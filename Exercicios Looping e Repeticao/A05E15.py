#Autor: Rodney Carneiro
#Data: 18/04/2022
#Objetivo: 
"""
Faça um algoritmo que seja capaz de armazenar as temperaturas médias diárias para um período
de 30 dias e que ao final informe: a maior temperatura; a menor temperatura; a temperatura
média; e o número de dias em que a temperatura ficou abaixo da média.
"""
maior = 0
menor = 999
soma = 0
menor_media = 0
for i in range(30):
    t = float(input("Digite a {} temperatura: ".format(i + 1)))
    soma = soma + t
    media = (soma / 30)

    if t > maior :
        maior = t
    if t < menor :
        menor = t
    if t < media :
        menor_media += 1
print("Média de temperatura = {}".format(media))
print("Maior temperatura = {}".format(maior))
print("Menor temperatura = {}".format(menor))
print("Dias com temperatura abaixo da média = {}".format(menor_media))
      
