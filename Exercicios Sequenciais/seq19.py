# Autor.....: Rodney Carneiro
# Data......: 17/04/2022
#Objetivo...: 
"""
Uma revendedora de carros usados paga a seus funcionários vendedores, um salário fixo por mês, 
mais uma comissão também fixa para cada carro vendido e mais 5% do valor das vendas por ele efetuadas.
Escrever um algoritmo que leia o número de carros por ele vendidos, o valor total de suas vendas, 
o salário fixo e a comissão que recebe por carro vendido. Escreva um algoritmo que calcule e 
escreva o salário mensal do vendedor. 
"""
#---- Programa Principal

#---- Entradas
carros = int(input("Digite a Quantidade de Carros vendidos..: "))
vendas = float(input("Digite o valor total das Vendas.........: "))
salario_fixo = float(input("Digite o Salario Fixo do Vendedor.......: "))
comissao = float(input("Digite o valor da Comissao por carro....: "))

#---- Processamento
salario = (salario_fixo + (vendas * 5/100)+ (carros * comissao))

#---- Saidas
print(f"O valor do Salario Mensal do vendor é de R$ {salario:.2f}")
