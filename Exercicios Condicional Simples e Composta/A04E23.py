# Autor.....: Rodney Carneiro
# Data......: 18/04/2022
# Objetivo..: Condicionais Simples e Complexas
"""
Faça um programa que lendo o nome, idade em anos e sexo de um associado de um clube concede 
desconto na mensalidade a ser paga, observando:
     sexo feminino  até 30 anos desconto  de 20% 
     sexo feminino  31 a 40 anos desconto de 30%
     sexo feminino  acima de 41 anos desconto de 35%

     sexo masculino até 25 anos sem desconto
     sexo masculino acima de 25 anos desconto de 25%.

Forneça nome, idade e mensalidade a pagar. 
 
"""

nome = str(input("Informe o nome....................: "))
idade = int(input("Informe a idade em anos...........: "))
sexo = str(input("Informe o sexo (M, F).............: "))
mensalidade = float(input("Informe o valor da mensalidade....: "))

if (sexo == "F"):
    if(idade <= 30):
        desconto = mensalidade - (mensalidade * 0.2)

    elif (idade >= 31) and (idade <=40):
        desconto = mensalidade - (mensalidade * 0.3)

    elif (idade > 41):
        desconto = mensalidade - (mensalidade * 0.35)
        print("{}, {}, {}" .format(nome, idade, desconto))

elif (sexo == "M"):
    if(idade <= 25):
        print("Sem desconto")
    elif(idade > 26):
        desconto = mensalidade - (mensalidade * 0.25)
        print("{}, {}, {}" .format(nome, idade, desconto))

else:
    print("Impossível identificar")
        
    
