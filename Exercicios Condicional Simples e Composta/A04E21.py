# Autor.....: Rodney Carneiro
# Data......: 18/04/2022
# Objetivo..: Condicionais Simples e Complexas
"""
Faça um programa que simula uma calculadora através de um menu de opções para as quatro operações : 
adição, multiplicação, divisão e subtração. Admita tipo real para os dados de entrada. 
"""

print ('+==========================================!')
print ('!            A - SOMA                      !')
print ('!            B - SUBTRAÇÃO                 !')
print ('!            C - MULTIPLICAÇÃO             !')
print ('!            D - DIVISÃO                   !')

opcao = str(input('!           Digite Sua opcao...: '))
print ('+==========================================+')

if (opcao != ("A" or "B" or "C" or "D")):
    print ("Impossivel calcular")

else:
    a = int(input("Informe um valor real.....: "))
    b = int(input("Informe um valor real.....: "))

    if (opcao == "A"):
        eq = a + b

    elif (opcao == "B"):
        eq = a - b

    elif (opcao == "C"):
        eq = a * b

    elif (opcao == "D"):
        eq = a / b

print ("{}" .format(eq))
