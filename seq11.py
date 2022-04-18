# Autor.....: Rodney Carneiro
# Data......: 17/04/2022
#Objetivo...: 
"""
Dado o preço de um produto em reais, converter este valor para o equivalente em dólares.
 O programa deverá ler o preço e a taxa de conversão para o dólar.  
"""

#---- Programa Principal

#---- Entradas
preco_real = float(input("Digite o valor do Produto em Reais.: "))
cotacao = float(input("Digite a cotacao do Dolar em R$....: "))

#---- Processamento

qtde_dolar = preco_real / cotacao

#---- Saidas
print(f"O Valor convertido em Dolar é {qtde_dolar:.2f}")
