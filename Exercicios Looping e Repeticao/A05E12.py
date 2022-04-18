#Autor: Rodney Carneiro
#Data: 18/04/2022
#Objetivo: 
"""
Elaborar um programa que efetue a leitura de 15 valores numéricos inteiros e no final apresente
o total do somatório da fatorial de cada valor lido.
"""

soma=0
for c in range (0,15):
     n=int(input('Digite o {}º valor..: '.format(c+1)))
     fat=1
     for i in range(n,0,-1):
          fat=fat*i
     print('O fatorial de {} é {}'.format(n,fat))
     soma=soma+fat
print('A soma do fatorial dos númeors é {}'.format(soma))

