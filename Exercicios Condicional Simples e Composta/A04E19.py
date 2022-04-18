# Autor.....: Rodney Carneiro
# Data......: 18/04/2022
# Objetivo..: Condicionais Simples e Complexas
"""
Dados o número de identificação do funcionário (alfanumérico com 8 caracteres), valor que ganha por 
hora, o número de horas-faltas e o número de horas-extras (considerar horas e minutos real ex: 8.30).
No final do programa imprimir o numero do funcionário e o prêmio a que faz juz. 
"""

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
           

