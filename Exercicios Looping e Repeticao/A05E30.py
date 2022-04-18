#Autor: Rodney Carneiro
#Data: 18/04/2022
#Objetivo: 
"""
Escrever um algoritmo que leia um número não determinado de valores e calcule a média
aritmética dos valores lidos, a quantidade de valores positivos, a quantidade de valores
negativos e o percentual de valores negativos e positivos. Mostre os resultados.
"""
soma = 0
cont = 0
qt_positivo = 0
qt_negativo = 0
while True:
    num=int(input("Digite um valor..: "))
    soma = soma + num
    cont = cont + 1
    if (num > 0):
        qt_positivo = qt_positivo + 1
    else:
        qt_negativo = qt_negativo + 1
    resp=str(input("Deseja continuar (S/N).: "))
    if (resp.upper() == "N"):
        break

media = soma / cont
perc_positivo = (qt_positivo / cont) * 100
perc_negativo = (qt_negativo / cont) * 100

print("-="*30)
print(f"Total de Numeros Lidos..........: {cont}")
print(f"A media Geral dos Numeros Lidos.: {media:.2f}")
print(f"Quantidade de Numeros Positivos.: {qt_positivo} ")
print(f"Percentual de Valors Positivos..: {perc_positivo:.2f}%")
print(f"Quantidade de Numeros Negativos.: {qt_negativo} ")
print(f"Percentual de Valors Negativos..: {perc_negativo:.2f}%")


