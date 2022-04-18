# Autor.....: Rodney Carneiro
# Data......: 17/04/2022
#Objetivo...: 
"""
Considere que o aumento dos funcionários de uma empresa é de 8% do salário atual mais um
percentual de produtividade discutido com a empresa. Escrever um algoritmo que lê o número 
do funcionário, seu salário atual, e o índice de produtividade discutido com a empresa.
Então, escreve o número do funcionário, seu aumento e o valor de seu novo salário.  
"""
#---- Programa Principal

#---- Entradas
nr_funcionario = int(input("Digite o Numero do Funcionario..: "))
salario=float(input("Digite o Salario do Funcionario........: "))
perc_produtividade=float(input("Digite o Percentual Produtividade......: "))

#---- Processamento
novo_salario = (salario * 1.08)* (1+(perc_produtividade/100))

#---- Saida
print(f"O novo Salario é {novo_salario:.2f}")