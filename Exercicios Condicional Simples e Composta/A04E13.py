# Autor.....: Rodney Carneiro
# Data......: 18/04/2022
# Objetivo..: Condicionais Simples e Complexas
"""
Faça um programa que , dados três valores, L1, L2 e L3, informa a área do triângulo por eles formado.
• Para que um valor possa ser lado de um triângulo ele não pode superar a soma dos outro dois valores.
Sp = (L1+L2+L3)/2
      
A =  (Sp x  (Sp - L1) x ( Sp - L2 ) x  (Sp - L3) )

(Fórmula de Héron - cálculo da área de um triângulo qualquer).

"""

L1 = float(input("Informe um valor....: "))
L2 = float(input("Informe um valor....: "))
L3 = float(input("Informe um valor....: "))

if (L1 < (L2 +L3)) or (L2 < (L1 +L3)) or (L3 < (L2 +L1)):
    sp = (L1 + L2 + L3) / 2
    area = (sp * (sp - L1) * (sp - L2) * (sp - L3)) ** (1/2)
    print ("A área do triangulo é {}" .format(area))

else:
    print ("Não é possível calcular")
    

