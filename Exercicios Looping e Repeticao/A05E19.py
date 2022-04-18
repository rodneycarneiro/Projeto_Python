#Autor: Rodney Carneiro
#Data: 18/04/2022
#Objetivo: 
"""
A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o
salário e número de filhos.
A prefeitura deseja saber:
    a) média do salário da população;
    b) média do número de filhos;
    c) maior salário;
    d) percentual de pessoas com salário até R$100,00.
O final da leitura de dados se dará com a entrada de um salário negativo. (Use o comando
ENQUANTO-FAÇA)
"""

tot_salario = 0
tot_filhos = 0
tot_pessoas = 0
tot_100 = 0
salario = 9
maior_salario = 0

while salario > 0 :
    salario = float(input("Digite o salário: "))

    if salario > 0 :
        nr_filhos = int(input("Digite o número de filhos: "))

        tot_salario = tot_salario + salario
        tot_filhos = tot_filhos + nr_filhos
        tot_pessoas = tot_pessoas + 1

        if salario < 100 :
            tot_100 = tot_100 + 1

        if salario > maior_salario :
            maior_salario = salario


if tot_pessoas > 0 :
    media_salario = tot_salario / tot_pessoas
    media_filhos = tot_filhos / tot_pessoas
    perc_100 = (tot_100 / tot_pessoas) * 100
else:
    media_salario = 0
    media_filhos = 0
    perc_100 = 0

    
print("Média de salário da população: {:.2f}".format(media_salario))
print("Média do número de filhos : {:.2f}".format(media_filhos))
print("Maior salário: {}".format(maior_salario))
print("Percentual de pessoas com salário até R$100,00: {:.2f}".format(perc_100))
