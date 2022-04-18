# Autor.....: Rodney Carneiro
# Data......: 18/04/2022
# Objetivo..: Condicionais Simples e Complexas
"""
Efetuar a leitura de quatro números inteiros e apresentar os números que são 
divisíveis por 2 ou por 3. 

"""

n_1 = int(input("Informe um número1.....: "))
n_2 = int(input("Informe um número2.....: "))
n_3 = int(input("Informe um número3.....: "))
n_4 = int(input("Informe um número4.....: "))

if ((n_1 %2) == 0): 
    print ("O número1 {} é divisível por 2" .format(n_1))
if ((n_1 % 3) == 0):
    print ("O número1 {} é divisível por 3" .format(n_1))

if ((n_2 %2) == 0): 
    print ("O número2 {} é divisível por 2" .format(n_2))
if ((n_2 % 3) == 0):
    print ("O número2 {} é divisível por 3" .format(n_2))
