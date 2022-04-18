# Autor.....: Rodney Carneiro
# Data......: 18/04/2022
# Objetivo..: Condicionais Simples e Complexas
"""
Apartir do salário de um funcionário. Calcule o desconto do INSS, 
adotando as seguintes regras: Até R157,00 descontar 8%, acima deste valor descontar 9%. 

"""

salario = float(input("Informe o salário de um funcionário.....:"))

if (salario > 0 and salario <= 157.0):
    desconto = 0.08 * salario

elif (salario > 0 and salario > 157.0):
    desconto = 0.09 * salario

salario_total = salario - desconto

print ("O desconto do INSS é de R$ {}, e o salário total é de {} " .format(desconto, salario_total))

