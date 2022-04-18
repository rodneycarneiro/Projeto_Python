# Autor.....: Rodney Carneiro
# Data......: 18/04/2022
# Objetivo..: Condicionais Simples e Complexas
"""
Ler quatro valores referentes a quatro notas escolares de um aluno e imprimir uma mensagem dizendo 
que o aluno foi aprovado, se o valor da media escolar for maior ou igual a 7. 
Se o valor da media for menor que 7 mostrar a mensagem que o aluno reprovou. 

"""

n_1 = float(input("Informe a nota do aluno.....: "))
n_2 = float(input("Informe a nota do aluno.....: "))
n_3 = float(input("Informe a nota do aluno.....: "))
n_4 = float(input("Informe a nota do aluno.....: "))

media = (n_1 + n_2 + n_3 + n_4) / 4

if ((media > 7) or (media == 7)):
    print ("O aluno está aprovado")

else:
    print("O aluno está reprovado")
    
