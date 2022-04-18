# Autor.....: Rodney Carneiro
# Data......: 17/04/2022
#Objetivo...: 
"""
Fazer um algoritmo para ler duas notas, os pesos de cada nota e mostrar a média ponderada.
Média Ponderada = ((nota 1 * peso da nota 1) + (nota 2 * peso da nota 2) / (soma dos pesos);

Apresentar ao final no formato:

A MEDIA PONDERADA É XXXX;

"""
#---- Programa Principal

#---- Entradas
nota1=float(input("Digite a 1. Nota...: "))
nota2=float(input("Digite a 2. Nota...: "))
nota3=float(input("Digite a 3. Nota...: "))
peso1=float(input("Digite o Peso1.....: "))
peso2=float(input("Digite o Peso2.....: "))
peso3=float(input("Digite a Peso3.....: "))

#---- Processamento
media_ponderada = ((nota1*peso1)+(nota2*peso2)+(nota3*peso3))/ (peso1+peso2+peso3)

#---- Saida
print(f"A Media Ponderada é {media_ponderada:.2f}")