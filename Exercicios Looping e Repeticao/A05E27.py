#Autor: Rodney Carneiro
#Data: 18/04/2022
#Objetivo: 
"""
Escreva um algoritmo que leia um número n (número de termos de uma progressão
aritmética), a1 ( o primeiro termo da progressão) e r (a razão da progressão) e escreva
os n termos desta progressão, bem como a soma dos elementos.

DEFINIÇÃO
Consideremos a seqüência ( 2, 4, 6, 8, 10, 12, 14, 16).
Observamos que, a partir do segundo termo, a diferença entre qualquer termo e seu antecessor é 
sempre a mesma:
    4 – 2 = 6 – 4 = 10 – 8 = 14 – 12 = 16 – 14 = 2
"""

a1=int(input("Digite o Primeiro Termo da Progressao Aritmetica.: "))
n=int(input("Digite o numero de Termos da Progressa Aritmetica..: "))
r=int(input("Digite a Razao da Progressao Aritmetica............: "))

print("-="*30)
cont = 0
while (cont < n):
    print(a1,end=" - ")
    a1 = a1 + r
    cont = cont + 1