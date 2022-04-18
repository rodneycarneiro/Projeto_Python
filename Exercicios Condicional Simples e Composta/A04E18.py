# Autor.....: Rodney Carneiro
# Data......: 10/05/
# Objetivo..: Condicionais

a = int(input("Informe um valor inteiro....: "))
b = int(input("Informe um valor inteiro....: "))
c = int(input("Informe um valor inteiro....: "))

if ((a > b) and (a > c)):
    if (b > c):
        print (" {} {} {} " .format(c, b, a))
    else:
        print (" {} {} {} " .format(b, c, a))

elif ((b > a) and (b > c)):
    if (a > c):
        print (" {} {} {} " .format(c, a, b))
    else:
        print (" {} {} {} " .format(a, c, b))

elif ((c > a) and (c > b)):
    if (a > b):
        print (" {} {} {} " .format(b, a, c))
    else:
        print (" {} {} {} " .format(a, b, c))

else:
    print ("Impossível executar")
