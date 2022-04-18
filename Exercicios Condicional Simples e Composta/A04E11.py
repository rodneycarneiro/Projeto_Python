# Autor.....: Rodney Carneiro
# Data......: 18/04/2022
# Objetivo..: Condicionais Simples e Complexas
"""
Dado um número inteiro positivo identificar se o mesmo é par, ímpar, múltiplo de 3, múltiplo de 5 ou 
múltiplo de 7.  

"""

n = int(input("Informe um número inteiro positivo.....: "))

if (n % 2 == 0):
    print("O número {} é par" .format(n))

else:
    print("O número {} é impar" .format(n))

if (n % 3 == 0):
    print("O número {} é múltiplo de 3" .format(n))

if (n % 5 == 0):
    print("O número {} é múltiplo de 5" .format(n))

if (n % 7 == 0):
    print("O número {} é múltiplo de 7" .format(n))
    
