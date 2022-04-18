#Autor: Rodney Carneiro
#Data: 18/04/2022
#Objetivo: 
"""
Apresentar os resultados de uma tabuada de um número qualquer. Esta deverá ser impressa no
seguinte formato:
Considerando como exemplo o fornecimento do número 02.
     2 x 1 = 2
     2 x 2 = 4
     .
     .
     2 x 10 = 20
"""
num = int(input("Digite o número a ser calculado na tabuada: "))
valor_inicial = int(input("Digite o valor inicial: "))
valor_final = int(input("Digite o valor final: "))
passo = int(input("Digite o passo: "))

for i in range(valor_inicial, valor_final + 1, passo):
    result = num * i
    print("{} * {} = {}".format(num, i, result))
