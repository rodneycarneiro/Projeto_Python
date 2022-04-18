#Autor: Rodney Carneiro
#Data: 18/04/2022
#Objetivo:
"""
Apresentar o total da soma obtida dos cem primeiros números inteiros (1+2+3......98+99+100)
"""
soma = 0

for i in range(0,101):
    soma = soma + i
print("A soma dos valores é {}".format(soma))
