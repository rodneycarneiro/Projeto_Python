#Autor: Rodney Carneiro
#Data: 18/04/2022
#Objetivo: 
"""
Escrever um algoritmo que leia um número n que indica quantos valores devem ser lidos a
seguir. Para cada número lido, mostre uma tabela contendo o valor lido e o fatorial deste valor.
"""

n=int(input("Digite um valor para N.: "))
for x in range(n):
    numero=int(input(f"Digite o {x+1}. valor.: "))
    fat = 1
    for c in range(1,numero+1,1):
        fat = fat * c
    
    print(f" . O Numero {numero} tem fatorial é {fat}")
        