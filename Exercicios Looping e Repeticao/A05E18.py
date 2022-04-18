#Autor: Rodney Carneiro
#Data: 18/04/2022
#Objetivo.: 
"""
Escrever um algoritmo que lê 5 valores para a, um de cada vez, e conta quantos destes valores
são negativos, escrevendo esta informação.
"""

soma = 0
for c in range(0,5):
    a=float(input('Digite um valor...: '))
    if a<0:
        soma<=soma+1
        print('O valor {} é Negativo'.format(a))

print('O Total de Numeros negativos é {}'.format(soma))
        
        
