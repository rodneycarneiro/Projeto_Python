# Autor.....: Rodney Carneiro
# Data......: 17/04/2022
#Objetivo...: 
"""
Uma empresa tem para um determinado funcionário uma ficha contendo o nome, número de horas 
trabalhadas e o numero de dependentes de um funcionário. Considerando que:
    a) A empresa paga 12 reais por hora e 40 reais por dependentes.
    b) Sobre o salário são feito descontos de 8,5% para o INSS e 5% para IR.

Faça um algoritmo para ler o Nome, número de horas trabalhadas e número de dependentes de um 
funcionário. 
Após a leitura, escreva qual o Nome, salário bruto, os valores descontados para cada tipo de 
imposto e finalmente qual o salário líquido do funcionário.
"""

#---- Programa Principal

#---- entrada
nome=str(input("Digite o nome do Funcionario....: ")) 
horas=int(input("Digite a Qtde Horas Trabalhadas.: "))
dependentes = int(input("Digite a Qtde Dependentes......: "))

#---- Processamento
salario = (horas * 12) + (dependentes * 40)
inss = salario * (8.5 / 100)
ir   = salario * (15 / 100)
salario_liquido = salario - inss - ir

#---- Saidas
print(f"Nome do Funcionario...: {nome}")
print(f"Salario Bruto.........: {salario:.2f}")
print(f"O valor do INSS.......: {inss:.2f}")
print(f"O valor O IR..........: {ir:.2f}")
print(f"O salario Liquido.....: {salario_liquido:.2f}")

