# Autor.....: Rodney Carneiro
# Data......: 17/04/2022
#Objetivo...: 
"""
O preço de um automóvel é calculado pela soma do preço de fábrica com o preço dos impostos
 (45% do preço de fábrica) e a percentagem do revendedor (28% do preço de fábrica). 
Faça um algoritmo que leia o nome do automóvel e o preço de fábrica e escreva  o nome do 
automóvel e o preço final. 
"""

#---- Programa Principal

#---- Entradas
automovel=str(input("Digite a marca do Automovel..: "))
preco_fabrica = float(input("Digite o Preco de Fabrica..: "))

#---- Processamento
impostos = (preco_fabrica * 45 / 100)
perc_revendedor = (preco_fabrica * 28 / 100)
preco_final = preco_fabrica + impostos + perc_revendedor

#---- Saidas
print(f"A marca do automovel...: {automovel}")
print(f"O preco Final..........: {preco_final:.2f}")
