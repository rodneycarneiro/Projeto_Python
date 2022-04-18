# Autor.....: Rodney Carneiro
# Data......: 18/04/2022
# Objetivo..: Condicionais Simples e Complexas
""""
Ler uma variável e somar 5 a ela caso seja positiva e somar 8 caso seja negativa. 
"""

variavel = float(input("Informe uma variável.....: "))

soma = 0
if (variavel > 0):
    soma = variavel + 5
    print ("A soma é = {}" .format(soma))
elif (variavel < 0):
    soma = variavel + 8
    print ("A soma é = {}" .format(soma))

else:
    print ("Não é possível executar a soma")
