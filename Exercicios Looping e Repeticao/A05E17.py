#Autor: Rodney Carneiro
#Data: 18/04/2022
#Objetivo: 
"""
Faça um algoritmo que permita ao usuário preencher uma tabela de caracteres de tamanho 30 e
ao final verifique a quantidade de caracteres 'z' inseridos na mesma.
"""
c = 0
for i in range(30):
    carac = input("Digite o {} caractere: ".format(i + 1))

    if carac == "z" :
        c = c + 1
print("Quantidade de caracteres z = {}".format(c))

