# Autor.....: Rodney Carneiro
# Data......: 17/04/2022
#Objetivo...: 
""""
Dado as seguintes informações de um funcionário:  Nome, idade cargo e o seu salário bruto considere:
    a) O salário bruto teve um reajuste de 38%.
    b) O funcionário receberá uma gratificação de 20% do salário bruto.
    c) O Salário total é descontado em 15%
Faça um algoritmo e um algoritmo para:
    • Imprimir Nome, idade e cargo.
    • Imprimir o salário bruto.
    • Imprimir o salário líquido.
"""

#---- Programa Principal
#---- Entradas
nome=str(input("Digite o Nome...........: "))
idade=int(input("Digite a Idade..........: "))
cargo=str(input("Digite o Cargo..........: "))
salario=float(input("Digite o Salario Bruto..: "))

#---- Processamento
gratificacao = salario * 20 / 100
novo_salario = salario + (salario * (38 / 100))
desconto = (novo_salario + gratificacao ) * ( 15/100)
salario_liquido = novo_salario + gratificacao - desconto

#---- Saida
print(f"Nome do funcionario..: {nome}")
print(f"Idade................: {idade}")
print(f"Cargo................: {cargo}")
print(f"Salario Bruto........: {salario:.2f}")
print(f"Salario Liquido......: {salario_liquido:.2f}")

