#Autor: Rodney Carneiro
#Data: 18/04/2022
#Objetivo: 
"""
Escrever um algoritmo que leia 20 valores para uma variável n e, para cada um deles, calcule a
tabuada de 1 até n. Mostre a tabuada na forma:
    1 x n = n
    2 x n = 2n
    3 x n = 3n
    .......
    n x n = n2
"""
for i in range(20):
    n=int(input("Digite um valor para N.: "))
    for x in range(1,n+1,1):
        print(f"  {x} x {n} = {x*n}")
        