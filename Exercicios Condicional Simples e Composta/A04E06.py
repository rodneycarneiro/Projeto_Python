# Autor.....: Rodney Carneiro
# Data......: 18/04/2022
# Objetivo..: Condicionais Simples e Complexas
"""
Elaborar a leitura de um número inteiro e apresentar uma mensagem informando
se o número é par ou impar. 

"""

n = int(input("Informe um número inteiro....: "))

if ( n%2==0):
    print ("O número {} é par" .format(n))
else:
    print ("O número {} é impar" .format(n))
