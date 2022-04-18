#Autor: Rodney Carneiro
#Data: 18/04/2022
#Objetivo: 
"""
Escreva um algoritmo que leia 50 valores e encontre o maior e o menor deles. Mostre o resultado.
"""

maior = 0
menor = 0
somatoria = 0
for i in range (50):
    valor = float(input("Digite o valor: "))
    somatoria = somatoria + valor
    if (menor > valor):
        menor = valor
    if (maior < valor):
        maior = valor
print("O menor valor é:{}".format (menor))
print("O maior valor é:{}".format (maior))
print("A somatoria é: {}".format(somatoria))
