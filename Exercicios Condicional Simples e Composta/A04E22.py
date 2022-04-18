# Autor.....: Rodney Carneiro
# Data......: 18/04/2022
# Objetivo..: Condicionais Simples e Complexas
"""
Faça um programa que analisa a quantidade de peças vendidas por um funcionário de uma loja com a 
finalidade de conceder gratificação no salário dentro dos parâmetros:
        até 30          - sem gratificação;
        31 a 60         - 10% sobre o salário;
        61 a 100        - 15% sobre o salário;
        101 a 150       - 20% sobre o salário;
        mais de 150     - 30% sobre o salário.
Fornecer saída tipo: Funcionário João das Dores gratificação R$ ____ , __ Salário total R$______, ___
Obs.: Será necessário ler o nome do Funcionario, seu salario por mes e a quantidade de  peças vendidas 
"""


nome = str(input("Informe o nome do funcionário...........................: "))
pecas = int(input("Informe o número de peças que o funcionário vendeu......: "))
salario = float(input("Informe o salário do funcionário........................: "))

if (pecas >= 0) and (pecas <= 30):
    print("Funcionário: ", nome)
    print("Gratificação: sem gratificação")
    print("Salário total R$ ", salario)

elif (pecas >= 31) and (pecas <= 60):
    gratificacao = 0.10 * salario

elif (pecas >= 61) and (pecas <= 100):
    gratificacao = 0.15 * salario
    
elif (pecas >= 101) and (pecas <= 150):
    gratificacao = 0.20 * salario

else :
    gratificacao = 0.30 * salario
total = gratificacao + salario

print("Funcionário: ", nome)
print("Gratificação: ", gratificacao)
print("Salário total R$ ", total)
