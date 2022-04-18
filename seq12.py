# Autor.....: Rodney Carneiro
# Data......: 17/04/2022
#Objetivo...: 
"""
Dados três valores, calcular e escrever as médias aritmética e harmônica destes valores.
OBS: média harmônica:       3
                        -----------
                          1 + 1 + 1
                          A   B   C

"""

#---- Programa Principal

#---- Entradas
a = int(input("Digite o valor de A...: "))
b = int(input("Digite o valor de B...: "))
c = int(input("Digite o valor de C...: "))

#---- Processamennto

media_harmonica = (3 / ((1/a)+(1/b)+(1/c)))

#saidas
print(f"A Media Harmonica calculada é {media_harmonica:.2f}")
