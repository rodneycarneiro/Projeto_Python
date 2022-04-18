# Autor.....: Rodney Carneiro
# Data......: 10/05/
# Objetivo..: Condicionais

funcionario = int(input("Informe o número do funcionário.........: "))
valor_hr = float(input("Informe o valor que ganha por horas.....: "))
hr_falta = float(input("Informe  número de horas falta..........: "))
hr_extra = float(input("Informe o número de horas extras........: "))

hr = hr_extra - hr_falta

if (hr > 0):
    premio = hr * valor_hr
    print ("Número do funcionário.....: {}. O prêmio que o funcionário faz juz é R$ {}" .format(funcionario, premio))

else:
    print ("O funcionário não receberá premio algum")
           

