# Autor.....: Rodney Carneiro
# Data......: 17/04/2022
#Objetivo...: 
"""
Escreva um algoritmo que leia três números inteiros e positivos (A, B, C) e calcule a seguinte expressão: 
    D = R+S        
         2
    Onde: R = (A+B) ^2
          S = (B+C) ^2
"""

#---- Programa Principal

#---- Entradas
a = int(input("Digite o Valor de A.: "))
b = int(input("Digite o Valor de B.: "))
c = int(input("Digite o valor de C.: "))

#---- Processamento

r = (a + b) ** 2
s = (b + c) ** 2
d = (r + s) / 2

#---- Saida
print(f"O valor de R é {r:.2f}")
print(f"O valor de S é {s:.2f}")
print(f"O valor de D é {d:.2f}")
