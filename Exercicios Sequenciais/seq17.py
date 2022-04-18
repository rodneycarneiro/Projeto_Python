# Autor.....: Rodney Carneiro
# Data......: 17/04/2022
#Objetivo...: 
"""
Um motorista de taxi deseja calcular o rendimento de seu carro na praça. Sabendo-se que o preço do 
combustível é de R$ 7,00 , escreva um algoritmo para ler: a marcação do odômetro (Km) no início do
dia, a marcação (Km) no final do dia, o número de litros de combustível gasto e o valor total (R$)
recebido dos passageiros. Calcular e escrever: a média do consumo em Km/L e o lucro (líquido) do dia. 
"""
#---- Programa Principal

#---- Entradas
km_inicio = int(input("Digite a Kilometragem Inicial...: "))
km_final  = int(input("Digite a Kilometragem Final.....: "))
litros    = int(input("Digite a Qtde Litros Combustivel: "))
valor_rec = float(input("Digite o valor recebido.......: "))

#---- Processamento
valor_gasto = (litros * 7)
media_consumo = (km_final - km_inicio) / litros
lucro = valor_rec - valor_gasto

#---- Saidas
print(f"A media de Consumo é de {media_consumo:.2f} km/litro")
print(f"O Lucro obtido R$ {lucro:.2f}")

