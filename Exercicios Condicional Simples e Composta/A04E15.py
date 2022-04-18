# Autor.....: Rodney Carneiro
# Data......: 18/04/2022
# Objetivo..: Condicionais Simples e Complexas
"""
Faça um programa que lê o nome de um funcionário, as horas por ele trabalhadas e seu salário/hora. 
O programa deverá informar o salário final do funcionário, considerando 50% de acréscimo para horas
extras. 
Considere como padrão 40 horas semanais. 
"""

nome = str(input("Informe o nome do funcionário.......: "))
horas = int(input("Informe as horas que ele trabalhou..: "))
salario_hr = float(input("Informe seu salário por hora........: "))

if (horas > 40):
    hr_extra = horas - 40
    salario_total = (40 * salario_hr) + (hr_extra * salario_hr) + (hr_extra * (salario_hr * 0.5))

elif (horas == 40):
    salario_total = 40 * salario_hr

else:
    salario_total = horas * salario_hr

print ("Nome.....: {}, O salário final desse funcionário é R$ {}" .format(nome, salario_total))
