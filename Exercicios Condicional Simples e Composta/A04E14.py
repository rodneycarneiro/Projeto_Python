# Autor.....: Rodney Carneiro
# Data......: 18/04/2022
# Objetivo..: Condicionais Simples e Complexas
"""
Faça um programa que calcula as raízes de uma equação do 2º grau sendo:

               x =  ( - b +- (b2 - 4ac) ) /  2a.

Observe que o cálculo não será possível:
. Quando a for = zero emitir a mensagem (divisão por zero);
. Quando Raiz (b2 - 4ac) for menor que zero emitir a mensagem(teremos raízes imaginárias).
"""

a = float(input("Informe um valor.....: "))
b = float(input("Informe um valor.....: "))
c = float(input("Informe um valor.....: "))

delta = ((b **2) - 4 * a * c)

if (a == 0):
    print("Divisão por zero")

elif (delta < 0):
    print("Teremos raízes imaginárias")

else:
    x1 = (-b - (((delta) ** 2) - 4 * a * c)) / 2 * a
    x2 = (-b + (((delta) ** 2) - 4 * a * c)) / 2 * a
    print ("X_1: {}, X_2: {}" .format(x1, x2))
