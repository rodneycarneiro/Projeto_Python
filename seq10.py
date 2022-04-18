# Autor.....: Rodney Carneiro
# Data......: 17/04/2022
#Objetivo...: 
"""
Faça um programa que leia a idade de uma pessoa expressa em anos, meses e dias e mostre-a expressa
 apenas em dias. Assuma, neste programa, que um ano tem 365 dias e que um mês tem 30 dias. 
"""

#---- Programa Principal

#---- Entradas
anos=int(input("Digite quantidade de Anos.....: "))
meses=int(input("Digite a quantidade de Meses..: "))
dias =int(input("Digite a Quantidade de dias...: "))

#---- Processamento

total_dias = ((anos * 365) + (meses * 30) + dias)

#---- Saidas
print(f"Uma pessoa com {anos} anos {meses} meses e {dias} dias, totaliza {total_dias} dias")