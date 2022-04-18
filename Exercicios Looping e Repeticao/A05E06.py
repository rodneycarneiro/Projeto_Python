#Autor: Rodney Carneiro
#Data: 18/04/2022
#Objetivo: Mostrar os números entre 0 e 200 divisíveis por 4 usando if
"""
Apresentar todos os números divisíveis por 4 que sejam menores que 200. Para verificar se o
número é divisível, sendo, mostre-o, não sendo, passe para o próximo passo. A variável que
controlará o contador deverá ser iniciada com valor 1
"""

for i in range(1,201):
    if i % 4 == 0 :
        print(i)
