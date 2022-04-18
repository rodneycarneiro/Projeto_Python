# Autor.....: Rodney Carneiro
# Data......: 17/04/2022
#Objetivo...: 
#            Efetuar o cálculo e a apresentação do valor de uma prestação em atraso, utilizando a 
#            fórmula: PRESTACAO = VALOR + (VALOR * ( TAXA/100) * TEMPO) 

#----- Programa Principal
#----- Entradas
valor = float(input("Digite o valor..: "))
taxa= float(input("Digite a Taxa mensal.: "))
tempo = int(input("Digite o tempo.: "))

#---- Processamento
prestacao = valor + (valor * (taxa / 100)* tempo)

#---- Saida
print(f"O Valor da Prestacao em atraso é {valor:.2f} ")