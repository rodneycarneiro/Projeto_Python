#Autor: Rodney Carneiro
#Data: 18/04/2022
#Objetivo:
"""
Elaborar um programa que efetue a leitura sucessiva de valores numéricos e apresente no final
o total do somatório, a média e o total de valores lidos.
O programa deverá fazer as leituras dos valores enquanto o usuário estiver fornecendo valores
positivos, ou seja, o programa deverá parar quando o usuário fornecer um valor negativo (menor
que zero).
"""
soma = 0
media = 0
inicio = -1

while inicio < 0 :
    inicio = int(input("Digite o valor inicial: "))
    fim = int(input("Digite o valor final: "))

for i in range(inicio, fim + 1):
    soma = soma + i
    media = soma / ((fim + 1) - (inicio))

print("Soma = {}".format(soma))
print("Média = %.2f" % (media))
print("Total de valores lidos = {}".format((fim + 1) - (inicio)))
    
