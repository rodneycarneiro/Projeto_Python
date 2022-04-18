# Autor.....: Rodney Carneiro
# Data......: 17/04/2022
#Objetivo...: 
"""
Escrever um algoritmo que lê o número de um vendedor, o seu salário fixo, o total de vendas por
ele efetuadas e o porcentual que ganha sobre o total de vendas. 
Calcular o salário total do vendedor.
Escrever número do vendedor e o salário total. 
"""
#---- Programa Principal

#---- Entradas
vendedor=int(input("Digite o numero do Vendedor...: "))
salario=float(input("Digite o Salario Fixo........: "))
vendas=float(input("Digite Valor Total Vendas....: "))
percentual=float(input("Digite o Percentual Vendas...: "))

#---- Processamentos
salario_total = salario + (vendas * (percentual / 100))

#---- Saidas
print(f"O Salario total do vendodor é R$ {salario_total:.2f}")