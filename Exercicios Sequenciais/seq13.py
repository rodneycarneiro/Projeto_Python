# Autor.....: Rodney Carneiro
# Data......: 17/04/2022
#Objetivo...: 
"""
Faça um programa para calcular e imprimir o salário bruto a ser recebido por um funcionário em um mês.
O programa deverá utilizar os seguintes dados: número de horas que o funcionário trabalhou no mês, 
valor recebido por hora de trabalho e número de filhos com idade menor do que 14 anos 
(para adicionar o salário família de R$ 13,48 por filho). 
"""

#---- Programa Principal

#---- Entradas
horas=int(input( "Digite a Quantidade de Horas Trabalhadas.: "))
valor=float(input("Digite o Valor recebido por horas.......: "))
filhos=int(input("Digite a Quantidade de Filhos < 14 anos.: "))

#---- Processamento
salario = (horas * valor) + (filhos * 13.48)

#---- Saidas
print(f"Com {horas} trabalhadas a R$ {valor:.2f} e com {filhos} filhos Totaliza salario de R$ {salario:.2f}")
