#Autor: Rodney Carneiro
#Data: 18/04/2022
#Objetivo:
"""
Elaborar um programa que apresente no final o somatório dos valores pares existentes na faixa
de 1 até 500.
"""
soma = 0

for i in range(1,500):

    if i % 2 == 0 :
        soma = soma + i

print("A soma dos valores é {}".format(soma))