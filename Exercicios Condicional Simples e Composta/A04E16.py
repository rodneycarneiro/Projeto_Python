# Autor.....: Rodney Carneiro
# Data......: 18/04/2022
# Objetivo..: Condicionais Simples e Complexas
"""
Faça um programa que determina o menor entre três valores inteiros lidos. 

"""
v1 = int(input("Informe um valor.....: "))
v2 = int(input("Informe um valor.....: "))
v3 = int(input("Informe um valor.....: "))

if ((v1 < v2) and (v1 < v3)):
    print ("O menor número entre os três valores é {}" .format(v1))

elif ((v2 < v1) and (v2 < v3)):
    print ("O menor número entre os três valores é {}" .format(v2))

elif ((v3 < v2) and (v3 < v1)):
    print ("O menor número entre os três valores é {}" .format(v3))

else:
    print ("Impossível calcular")
