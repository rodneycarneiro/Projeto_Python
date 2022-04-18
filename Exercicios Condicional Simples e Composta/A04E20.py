# Autor.....: Rodney Carneiro
# Data......: 18/04/2022
# Objetivo..: Condicionais Simples e Complexas
"""
Uma empresa decidiu dar uma gratificação de Natal a seus funcionários, baseada no numero de horas 
extras e no número de horas que o empregado faltou ao trabalho. O valor do prêmio é obtido pela 
consulta a tabela abaixo, em que H é o número de horas extras subtraído do número de horas faltas.
H( horas)                              Prêmio (R$)
[0,10]                                       20,00
(10,20]                                      40,00
(20,30]                                      60,00
(30,40]                                      80,00
(40,100]                                    100,00
OBS.: O simbolo de parenteses ( indica valores maior que
          O simbolo de colchetes [ Indica inclusive 
Exemplo: (10,20] sao os valores maiores que 10 e menores ou iguais a 20 
"""

hr_extra = int(input("Informe o número de hora extra...: "))
hr_falta = int(input("Informe o número de hora falta...: "))

H = hr_extra - hr_falta

if (H >= 0) and  (H <= 10) :
    print ("A gratificação é de R$20,00")

elif (H > 10) and (H <=20):
    print ("A gratificação é de R$40,00")

elif (H > 20) and (H <=30):
    print ("A gratificação é de R$60,00")

elif (H > 30) and (H <=40):
    print ("A gratificação é de R$80,00")

elif (H > 40) and (H <=100):
    print ("A gratificação é de R$100,00")
