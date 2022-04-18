# Autor.....: Rodney Carneiro
# Data......: 17/04/2022
#Objetivo...: 
"""
Um hotel com 75 apartamentos deseja fazer uma promoção especial de final de semana, concedendo 
um desconto de 25% na diária. Com isto, espera aumentar sua taxa de ocupação de 50 para 80%. 
Sendo dado o valor normal da diária, calcular e imprimir: 
    a) o valor da diária promocional; 
    b) o valor total arrecadado com 80% de ocupação e diária promocional; 
    c) o valor total arrecadado com 50% de ocupação e diária normal; 
    d) a diferença entre estes dois valores.

"""
#---- Programas Principal

#---- Entradas
diaria = float(input("Informe o valor normal da diária...: "))

#---- Processamento

promocional = diaria - (diaria * 0.25)
p_80 = promocional * (75 * 0.8)
p_50 = diaria * (75 * 0.5)
diferencas = p_80 - p_50

#---- Saidas
print ("O valor da diária promocional é de R$ ", promocional)
print ("O valor arrecadado com 80% de ocupação e diária promocional é de R$ ", p_80)
print ("O valor arrecado com 50% de ocupação e diária normal é de R$ ", p_50)
print ("A diferença entre os dois valores é de R$ ", diferencas)