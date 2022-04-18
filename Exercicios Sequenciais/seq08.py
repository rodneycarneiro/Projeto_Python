# Autor.....: Rodney Carneiro
# Data......: 17/04/2022
#Objetivo...: 
"""
Faça um algoritmo que leia as 3 notas de um aluno e calcule a média final deste aluno. 
Considerar que a média é ponderada e que o peso das notas é: 2,3 e 5, respectivamente. 
"""

#---- Programa Principal

#---- Entradas
nota1 = float(input("Digite a Primeira Nota..: "))
nota2 = float(input("Digite a Segunda Nota...: "))
nota3 = float(input("Digite a Terceira Nota..: "))

#---- Processamento
media = ((nota1 * 2)+ (nota2 * 3) + (nota3 * 5)) / 10

#---- Saidas
print(f"A media das notas é {media:.2f}")
