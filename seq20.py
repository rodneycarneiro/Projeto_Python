# Autor.....: Rodney Carneiro
# Data......: 17/04/2022
#Objetivo...: 
"""
Uma loja vende bicicletas com um acréscimo de 50 % sobre o seu preço de custo.
Ela paga a cada vendedor 2 salários mínimos mensais, mais uma comissão de 15 % sobre o 
preço de custo de cada bicicleta vendida, dividida igualmente entre eles.
Escreva um algoritmo que leia o número de empregados da loja, o valor do salário mínimo, 
o preço de custo de cada bicicleta, o número de bicicletas vendidas, calcule e escreva:
O salário final de cada empregado e o lucro (líquido) da loja.  
"""
#---- Programa Principal

#---- Entradas
nr_func = int(input("Digite o numero de Funcionarios.........: "))
salario_minimo=float(input("Digite o valor do Salario Minimo........: "))
preco_custo=float(input("Digite o Custo da Bicicleta.............: "))
qtd_vendida=int(input("Digite a Quantidade bicicletas Vendidas.:  "))

#---- Processamento
total_vendas = (preco_custo * 1.50)*qtd_vendida
comissao = (preco_custo * 15/100) * qtd_vendida
salario_final = (salario_minimo * 2) + (comissao / nr_func)
lucro = total_vendas - (salario_final * nr_func)

#----- Saidas
print(f"O Salario final de cada funcionario e de R$ {salario_final:.2f}")
print(f"O Lucro da empresa foi de R$ {lucro:.2f}")