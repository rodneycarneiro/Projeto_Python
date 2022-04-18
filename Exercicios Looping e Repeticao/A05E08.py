#Autor: Rodney Carneiro
#Data: 18/04/2022
#Objetivo: 
"""
Elaborar um programa que apresente o valor de uma potência de uma base qualquer elevada a
um expoente qualquer, ou seja, de NM.
"""

n = int(input("Digite o valor da base: "))
m = int(input("Digite o valor do expoente: "))

total = 1

for i in range(1, m + 1):
    total = total * n
print("{} elevado a {} = {}".format(n, m, total))

