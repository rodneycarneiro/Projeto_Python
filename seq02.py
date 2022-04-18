# Autor.....: Rodney Carneiro
# Data......: 17/04/2022
#Objetivo...: 
# Elaborar um programa que efetue a apresentação da conversão em real (R$) 
# de um valor lido em dólar (US$). 
# O programa deverá solicitar o valor da cotação do dólar e também a quantidade de dólares
#  disponível com o usuário. 

#----- Programa Principal
#----- Entradas
cotacao = float(input("Digite a Cotacao do Dolar....: "))
qt_dolar=  int(input("Digite a Quantidade de Dolar.: "))

#---- Processamento
valor_reais = (cotacao * qt_dolar)

#---- Saidas
print(f"{qt_dolar} dolares convertidos na cotacao de R$ {cotacao:.2f} totaliza R$ {valor_reais:.2f} ")
