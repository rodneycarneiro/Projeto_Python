# Autor.....: Rodney Carneiro
# Data......: 17/04/2022
#Objetivo...: 
"""
Faça um algoritmo que mostre o resultado da expressão abaixo:

R:=(( x * 5) * y) * z

Obs: Ler valores para as variáveis x, y e z e no final mostrar o Valor de R.
 
"""
#---- Programa Principal

#---- Entradas
x=int(input("Digite o valor de X..: "))
y=int(input("Digite o valor de Y..: "))
z=int(input("Digite o valor de Z..: "))

#---- Processamento

r = ((x * 5)* y)*z

#---- Saidas
print(f"R:=(( x * 5) * y) * z")
print(f"(( {x} * 5) * {y}) * {z} = {r}")
