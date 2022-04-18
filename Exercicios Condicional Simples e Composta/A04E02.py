# Autor.....: Rodney Carneiro
# Data......: 18/04/2022
# Objetivo..: Condicionais Simples e Complexas
"""
Ler duas variáveis A e B, se a variável A for menor que B, fazer Y= B – A, se B for menor que A
fazer Y= A – B, caso sejam iguais fazer Y = A + B, imprimir no final os valores de A, B e Y. 
"""

A = float(input("Informe uma variável.....: "))
B = float(input("Informe uma variável ....: "))

if (A < B):
    Y = B - A

elif (B < A):
    Y = A - B

else:
    Y = A + B

print ("A = {}, B = {}, Y = {}" .format(A, B, Y))
