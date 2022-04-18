# Autor.....: Rodney Carneiro
# Data......: 17/04/2022
#Objetivo...: 
"""
A turma C é composta de 60 alunos, e a turma D de 20 alunos. Escreva um algoritmo que leia 
o percentual de alunos reprovados na turma C, o percentual de aprovados na turma D, 
calcule e escreva:
    a) O número de alunos reprovados na turma C.
    b) O número de alunos reprovados na turma D.
    c) A percentagem de alunos reprovados em relação ao total de alunos das duas turmas.

"""
#---- Programa Principal

#---- Entradas
perc_reprovado_c = float(input("Digite o Percentual de Reprovados Turma C.: "))
perc_reprovado_d = float(input("Digite o Percentual de Reprovados Turma D.: "))

#---- Processamento
alunos_reprovados_c = 60 * (perc_reprovado_c/100)
alunos_reprovados_d = 20 * (perc_reprovado_d/100)
total_reprovados = (alunos_reprovados_c + alunos_reprovados_d)
porcentagem =  (total_reprovados / 80)*100

#---- Saidas
print(f"Alunos reprovados da turma C foi de {alunos_reprovados_c:.2f}, sendo {perc_reprovado_c:.2f}%")
print(f"Alunos reprovados da turma D foi de {alunos_reprovados_d:.2f}, sendo {perc_reprovado_d:.2f}%")
print(f"Foram reprovados {total_reprovados:.2f} alunos, representando {porcentagem:.2f} por cento" )
