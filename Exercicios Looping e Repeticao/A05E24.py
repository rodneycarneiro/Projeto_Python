#Autor: Rodney Carneiro
#Data: 18/04/2022
#Objetivo: 
"""
Escreva um algoritmo que calcule a média dos números digitados pelo usuário, se eles forem
pares. Termine a leitura se o usuário digitar zero (0).
"""
soma = 0
cont = 0
while True:
    numero = int(input("Digite um numero (0=Fim)..: "))
    if (numero == 0):
        break
    elif (numero % 2 == 0):
        soma = soma + numero
        cont = cont + 1
if (cont > 0):
    media = soma / cont
else:
    media = 0
print(f"A soma dos Valores lidos é {soma} e a Media é {media:.2f}")