# Autor.....: Rodney Carneiro
# Data......: 17/04/2022
#Objetivo...: 
"""
Escreva um Algoritmo que dados os litros gastos e os quilômetros percorridos por um automóvel, 
calcule os gastos de combustível em Reais, calcule também qual a média de consumo que o carro 
teve durante a viagem.
(Considerar que um litro custa R$ 7,24) 
 
"""
#---- Programa Principal
km_percorridos = int(input("Digite a Quantidade de KM Percorridos.: "))
litros_gastos = int(input("Digite a Quantidade Litros Gastos.....: "))

#---- Entradas
gastos = litros_gastos * 7.24
media_consumo = km_percorridos / litros_gastos

#---- Saidas
print(f"O valor gasto de combustivel foi de R$ {gastos:.2f}")
print(f"A media de consumo do veiculo foi de {media_consumo:.2f}")