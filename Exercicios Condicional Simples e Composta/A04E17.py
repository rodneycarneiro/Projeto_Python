# Autor.....: Rodney Carneiro
# Data......: 18/04/2022
# Objetivo..: Condicionais Simples e Complexas
"""
Faça um programa que lê a hora inicial e final de um jogo, considerando apenas horas inteiras. 
Calcular a duração do jogo em horas, sabendo que o tempo máximo de duração de um jogo é de 24 horas 
e que o jogo pode começar em um dia e terminar no dia seguinte. 

"""

hr_inicial = int(input("Informe a hora inicial de um jogo.....: "))
hr_final = int(input("Informe a hora final de um jogo.......: "))


if (hr_inicial > hr_final):
    duracao = hr_final + (24 - hr_inicial)
    print("A duração de um jogo em horas é...: {}" .format(duracao))

elif (hr_inicial == hr_final):
    duracao = 24
    print("A duração de um jogo em horas é...:{}" .format(duracao))

else:
    duracao = hr_final - hr_inicial
    print ("A duração de um jogo em horas é...:{}" .format(duracao))
