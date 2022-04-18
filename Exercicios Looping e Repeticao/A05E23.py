#Autor: Rodney Carneiro
#Data: 18/04/2022
#Objetivo: 
"""
Escreva um algoritmo que calcule a média aritmética das 3 notas dos alunos de uma classe. O
algoritmo deverá ler, além das notas, o código do aluno e deverá ser encerrado quando o código
for igual a zero.
"""
while True:
    codigo=int(input("Digite o Codigo do Aluno..: "))
    if (codigo == 0):
        break
    else:
        nota1 =float(input("Digite a Primeira nota..: "))
        nota2 =float(input("Digite a Segunda nota...: "))
        nota3 =float(input("Digite a Terceira nota..: "))

        media = (nota1 + nota2 + nota3) / 3
        print(f"A Media do Aluno é {media:.2f} ")
