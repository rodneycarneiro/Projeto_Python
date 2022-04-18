# Autor.....: Rodney Carneiro
# Data......: 17/04/2022
#Objetivo...: 
"""
Maria quer saber quantos litros de gasolina precisa colocar em seu carro e quanto vai gastar para fazer uma viagem até a casa de sua irmã.
Dados extras:
   Distância da casa de Maria até sua irmã : 520 km
   Seu carro consome um litro a cada 12 Km rodado.
   Ela abastece sempre no mesmo posto, onde o preço da gasolina é R$ 7,20 o litro.

"""
#---- Programa Principal

#---- Processamento
media_litros = 520 / 12
valor_gasto = media_litros * 7.20

#---- Saida
print(f"A media de Litros de Combustivel é {media_litros:.2f}")
print(f"O valor Gasto sera de R$ {valor_gasto:.2f}")
