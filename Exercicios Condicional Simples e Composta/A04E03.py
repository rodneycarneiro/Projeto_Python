# Autor.....: Rodney Carneiro
# Data......: 18/04/2022
# Objetivo..: Condicionais Simples e Complexas
""""
Considerar três notas inteiras, encontrar a Média aritmética simples, entre as notas que correspondem 
aos números, deixando de fora da media as notas impares. Se nenhuma for PAR emita a
mensagem “NENHUMA NOTA PAR”. 
"""

n_1 = int(input("Informe uma nota....: "))
n_2 = int(input("Informe uma nota....: "))
n_3 = int(input("Informe uma nota....: "))

if ((n_1 % 2) == 0) and ((n_2 % 2) == 0) and ((n_3 % 2) == 0):
    media = (n_1 + n_2 + n_3) / 3
    print ("A média é igual a {}" .format(media))

elif ((n_1 % 2) == 0) and ((n_2 % 2) ==0) and ((n_3 % 2) != 0):
    media = (n_1 + n_2) / 2
    print ("A média é igual a {}" .format(media))

elif ((n_1 % 2) == 0) and ((n_3 % 2) ==0) and ((n_2 % 2) != 0):
    media = (n_1 + n_3) / 2
    print ("A média é igual a {}" .format(media))

elif ((n_3 % 2) == 0) and ((n_2 % 2) ==0) and ((n_1 % 2) != 0):
    media = (n_3 + n_2) / 2
    print ("{}" .format(media))

else:
    print ("Impossível calcular")
