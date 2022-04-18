#Autor: Rodney Carneiro
#Data: 18/04/2022
#Objetivo:
"""
Faça um algoritmo que armazene a descrição de 10 cargos e seus respectivos salários. Ao final,
o algoritmo deverá informar a descrição de um dos cargos e o respectivo salário do maior salario
digitado.
"""
maior = 0

for i in range(10):
    cargo = input("Digite o {} cargo: ".format(i + 1))
    salario = float(input("Digite o {} salário: ".format(i + 1)))

    if salario > maior :
        salario_maior = salario
        cargo_maior = cargo
print("Cargo: {}".format(cargo_maior))
print("Salário: {}".format(salario_maior))
