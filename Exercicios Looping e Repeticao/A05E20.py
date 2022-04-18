#Autor: Rodney Carneiro
#Data: 18/04/2022
#Objetivo: 
"""
Chico tem 1,50 metro e cresce 2 centímetros por ano, enquanto Zé tem 1,10 metro e cresce 3
centímetros por ano.
Construa um algoritmo que calcule e imprima quantos anos serão necessários para que Zé seja
maior que Chico.
"""
print("-="*30)
print(" Chico tem 1,50 m")
print(" Ze tem 1,10 m")
altura_chico = 1.50
altura_ze = 1.10
ano = 0
while (altura_ze < altura_chico):
    altura_ze = altura_ze + 0.03
    altura_chico = altura_chico + 0.02
    if (altura_ze < altura_chico):
        ano = ano + 1

print(f"Em {ano} anos Ze terá a altura maior do que Chico")
print(f" . Altura de Ze {altura_ze:.2f}")
print(f" . Altura de Chico {altura_chico:.2f}")
