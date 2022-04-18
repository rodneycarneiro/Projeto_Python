#Autor: Rodney Carneiro
#Data: 18/04/2022
#Objetivo:
"""
Apresentar todos os valores numéricos inteiros ímpares situados na faixa de 0 a 20. Para
verificar se o número é ímpar, efetuar dentro da malha a verificação lógica desta condição com a
instrução SE, perguntando se o número é ímpar, sendo, mostre-o, não sendo, passe para o
próximo passo.
"""

for i in range(0,21):
    if i % 2 != 0 :
        print(i)
