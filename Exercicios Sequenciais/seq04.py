# Autor.....: Rodney Carneiro
# Data......: 17/04/2022
#Objetivo...: 
"""
Faça um algoritmo para ler a base e a altura de um triângulo. Em seguida, escreva a área do mesmo.
Obs.:  Área = ( Base * Altura ) / 2
"""

#---- Programa Principal

#---- Entradas
base=float(input("Digite a base da Triangulo...: "))
altura=float(input("Digite a Altura do Triangulo.: "))

#---- Processamento
area = (base * altura) / 2

#---- Saida

print(f"A area do Triangulo de base {base:.2f} e altura {altura:.2f} e {area:.2f} ")