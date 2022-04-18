# Autor.....: Rodney Carneiro
# Data......: 18/04/2022
# Objetivo..: Condicionais Simples e Complexas
"""
Elaborar um algoritmo que efetue a leitura do nome e do sexo de uma pessoa, apresentando como 
saída uma das seguintes mensagens: “ILMO SR.” Para o sexo Masculino; “ILMA SRA.”, para o sexo feminino. 
Apresente também abaixo da mensagem o nome da pessoa. 

"""
nome = str(input("Informe o nome..................................: "))
sexo = str(input("Informe o sexo (Masculino (M), Feminino (F).....: "))

if (sexo  == "M"):
    print ("ILMO SR.")
    print ("{}" .format(nome))

elif (sexo == "F"):
    print ("ILMA SRA.")
    print ("{}" .format(nome))

else:
    print("Não é possivel identificar")
