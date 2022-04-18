#Autor: Rodney Carneiro
#Data: 18/04/2022
#Objetivo: 
"""
Construir um algoritmo que calcule a média aritmética de vários valores inteiros positivos, lidos
externamente.
O final da leitura acontecerá quando for lido um valor negativo.
"""

soma=0
num=0
cont=0
while (num>=0):
    num=int(input('Digite um número.: '))
    if(num>=0):
        soma=soma+num
        cont=cont+1
if(cont>0):    
    media=soma/cont
    print('Soma total {}/{} = média.: {:.2f}'.format(soma,cont,media))
else:
    print('Não foi digitado nenhum número positivo.')
