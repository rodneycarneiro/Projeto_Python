#Autor: Rodney Carneiro
#Data: 18/04/2022
#Objetivo:
"""
Apresentar as potências de 3 variando de 0 a 15. Deve ser considerado que qualquer número
elevado a zero é 1, e elevado a 1 é ele próprio. Deverá ser apresentado, observando a seguinte
definição:
     30 = 1
     31 = 3
     32 = 9
     (....)
     315 = 14348907
"""

for c in range(0,16):
     p=3**c
     print('3^{}={}'.format(c,p))
