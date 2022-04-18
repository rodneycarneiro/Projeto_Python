# Autor.....: Rodney Carneiro
# Data......: 18/04/2022
# Objetivo..: Condicionais Simples e Complexas
"""
Faça um programa que lê o nome de um aluno, suas três notas e fornece o conceito obtido em 
função da sua média considerando : nota1 - peso 2, nota2 - peso 3 nota3 - peso 5.
Média entre 0 - 4 (inclusive, inclusive) conceito D
Média entre 4 - 6 (exclusive , inclusive) conceito C
Média entre 6 - 8 (exclusive, inclusive ) conceito B
Média entre 8 - 10 (exclusive, inclusive) conceito A
"""

n_1 = float(input("Informe a primeira nota.....: "))
n_2 = float(input("Informe a segunda nota......: "))
n_3 = float(input("Informe a terceira nota.....: "))
p_1 = float(input("Informe o peso da nota 1....: "))
p_2 = float(input("Informe o peso da nota 2....: "))
p_3 = float(input("Informe o peso da nota 3....: "))

media = ((n_1 * p_1) + (n_2 * p_2) + (n_3 * p_3)) / (p_1 + p_2 + p_3)

if ((media >= 0) and (media <= 40)):
    print ("Conceito D")

elif ((media > 40) and (media <= 60)):
    print ("Conceito C")

elif ((media > 60) and (media <= 80)):
    print ("Conceito B")

elif ((media > 80) and (media <= 100)):
    print ("Conceito A")

else:
    print ("Impossiível identificar")
