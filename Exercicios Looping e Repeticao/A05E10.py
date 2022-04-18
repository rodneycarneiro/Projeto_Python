#Autor: Rodney Carneiro
#Data: 18/04/2022
#Objetivo: Conversão de Celsius para Fahrenheit  de 10 em 10
"""
Elaborar um programa que apresente os valores de conversão de graus Celsius para
Fahrenheit, de 10 em 10 graus. Iniciando a contagem em 10 graus Celsius e finalizando em 100
graus Celsius. O programa deverá apresentar os valores das duas temperaturas.
Observacao: Utilizar a formula F=(9*C+160)/5.
"""
for c in range (0,100,10):
     f=((9*c)+160)/5
     print('{}ºC = {}ºF'.format(c,f))
