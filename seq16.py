# Autor.....: Rodney Carneiro
# Data......: 17/04/2022
#Objetivo...: 
"""
A equipe Ferrari deseja calcular o número mínimo de litros que deverá colocar no tanque de
seu carro para que ele possa percorrer um determinado número de voltas até o primeiro reabastecimento.
Escreva um algoritmo que leia o comprimento da pista (em metros), o número total de voltas a serem
percorridas no grande prêmio, o número de reabastecimentos desejados, e o consumo de combustível
do carro (em Km/L). Calcular e escrever o número mínimo de litros necessários para percorrer até
o primeiro reabastecimento.
OBS: Considere que o número de voltas entre os reabastecimentos é o mesmo.
"""
#---- Programa Principal

#---- Entradas
comprimento = float(input("Informa o comprimento da pista em metros..........................: "))
numero_voltas = int(input("Informe o número de voltas a serem percorridas no grande prêmio...: "))
reabastecimento= int(input("Informe o número de reabastecimento desejados.....................: "))
consumo_combustivel = int(input("Informe o consumo de combustível do carro em Km/L.................: "))

#---- Processamento
numero_minimo = ((numero_voltas* comprimento) / consumo_combustivel) / reabastecimento

#---- Saidas
print ("O número mínimo de litros que deverá ser colocado no tanque de seu carro é ", numero_minimo,"L")
