#Autor: Rodney Carneiro
#Data: 18/04/2022
#Objetivo: 
"""
Escreva um programa que apresente a série de Fibonacci até o décimo quinto termo. A série de
Fibonacci é formada pela sequência: 1, 1, 2,3,5,8,13,21,34...etc. Esta série se caracteriza pela
soma de um termo posterior com o seu anterior subsequente.
"""
num1 = 1
num2 = 0
cont = 1
while cont <= 15:
    print(num1)
    num3 = num1
    num1 += num2
    num2 = num3
    cont += 1
