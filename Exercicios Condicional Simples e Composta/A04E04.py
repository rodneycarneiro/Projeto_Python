# Autor.....: Rodney Carneiro
# Data......: 18/04/2022
# Objetivo..: Condicionais Simples e Complexas
"""
Determinar num conjunto de 3 números o menor deles, imprimindo-o e também o maior deles. 

"""

x = float(input("Informe um número........: "))
y = float(input("Informe um número........: "))
z = float(input("Informe um número........: "))

if ((x > y) and (x > z)):
    print ("{} é o maior número" .format(x))
    
    if (y < z):
        print ("{} é o menor número" .format(y))
    else:
        print ("{} é o menor número" .format(z))

elif ((y > x) and (y > z)):
    print ("{} é o maior número" .format(y))

    if (x < z):
      print ("{} é menor número" .format(x))
    else:
      print ("{} é o menor número" .format(z))

elif ((z > x) and (z > y)):
      print ("{} é o maior número" .format(z))
      if (x < y):
        print ("{} é o menor número" .format(x))
      else:
        print("{} é o menor número" .format(y))

elif ((x == y) and (x == z) and (z == y)):
    ("Impossível identificar")

else:
    ("Impossível calcular")
      
      
      
        
