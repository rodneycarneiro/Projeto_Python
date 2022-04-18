#Autor: Rodney Carneiro
#Data: 18/04/2022
#Objetivo: 
"""
Escreva um algoritmo que leia o código de um aluno e suas três notas. Calcule a média
ponderada do aluno, considerando que o peso para a maior nota seja 4 e para as duas
restantes, 3. Mostre o código do aluno, suas três notas, a média calculada e uma mensagem
"APROVADO" se a média for maior ou igual a 5 e "REPROVADO" se a média for menor que 5.
Repita a operação até que o código lido seja negativo
Para calcular a media Ponderada, multiplique a primeira nota pelo peso1 e a segunda nota pelo
peso2, em seguinda some os dois valores e divida por 10.
"""

while True:
    codigo=int(input("Digite o Codigo do Aluno (oodigo -1 = Finaliza)..: "))
    if (codigo < 0):
        break
    else:
        media = -1
        nota1 =float(input("Digite a Primeira nota..: "))
        nota2 =float(input("Digite a Segunda nota...: "))
        nota3 =float(input("Digite a Terceira nota..: "))

        if (nota1 >= nota2) and (nota1 >= nota3):
            media = ((nota1*4 + (nota2 * 3) + (nota3*3)) / 10)
        elif (nota2 >= nota1) and (nota2 >= nota3):           
            media = ((nota2*4 + (nota1 * 3) + (nota3*3)) / 10)
        elif (nota3 >= nota1) and (nota3 >= nota2):           
            media = ((nota3*4 + (nota1 * 3) + (nota2*3)) / 10)

        print(f"Codigo do aluno é {codigo}")
        print(f". Primeira Nota foi {nota1:.2f}")
        print(f". Segunda Nota foi {nota2:.2f}")
        print(f". Terceira Nota foi {nota3:.2f}")
        print(f"A Media Ponderada do Aluno é {media:.2f} ")
        if (media >= 5):
            print("O Aluno esta Aprovado")
        else:
            print("O Aluno esta Reprovado")
