# Autor.....: Rodney Carneiro
# Data......: 17/04/2022
#Objetivo...: 
"""
O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem do
distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que a percentagem do
distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo que leia o custo de 
fábrica de um carro e escreva o custo ao consumidor. 
"""

#---- Programa Principal

#---- Entradas
preco_fabrica = float(input("Digite o Preco de Fabrica do Automovel..: "))

#---- Processamento
impostos = (preco_fabrica * 45 / 100)
perc_revendedor = (preco_fabrica * 28 / 100)
preco_final = preco_fabrica + impostos + perc_revendedor

#---- Saidas
print(f"O preco Final do automovel  é....: {preco_final:.2f}")
