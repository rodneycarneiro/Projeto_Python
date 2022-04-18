#Autor: Rodney Carneiro
#Data: 18/04/2022
#Objetivo: 
"""
Elaborar um programa que efetue o cálculo e no final apresente o somatório do número de grãos
de trigo que se pode obter num tabuleiro de xadrez, obedecendo a seguinte regra: Colocar um
grão de trigo para o primeiro quadro e, nos quadros seguintes o dobro do quadro anterior. Ou
seja, no primeiro quadro coloca-se 1 grão, no segundo quadro coloca-se 2 graos (neste
momento tem-se 3 grãos), no terceiro quadro coloca-se 4 grãos (tendo neste momento 7 grãos),
no quarto quadro coloca-se 8 grãos (tendo-se então 15 grãos) até atingir o sexagésimo quarto
quadro.
"""
s=0
for c in range(1,65):
     g=2**c
     s=s+g
     print(g)
print('A soma final é {}'.format(s))
     

