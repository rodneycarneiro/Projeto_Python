# Autor.....: Rodney Carneiro
# Data......: 18/04/2022
# Objetivo..: Condicionais Simples e Complexas
"""
Faça um programa que fornece o seguinte menu de opções:
A- Cálculo da área do círculo
B- Cálculo da área do retângulo
C- Cálculo da área do trapézio;
D- Cálculo da área do triângulo

Fornecer saída do tipo : 
“ A área do círculo de raio ______ é igual a ________ m2”
Obs.: . O programa deverá mostrar uma tela contendo as opçoes acima descritas.
         . Deverá ser lido as informações de acordo com a opção selecionada, ou seja, para calcular a area de um retangulo devera usar a formula:  
AREA = Lado X Altura, portado devera ser lido as variaveis Lado e Altura.
OBS2:  Pesquisar nos livros de matematica as formulas para calculo das demais areas 

"""

print ('+================================================================+')
print ('!                                                                !')
print ('!            A - Calculo da Area do Circulo                      !')
print ('!            B - Calculo da Area do Retangulo                    !')
print ('!            C - Calculo da Area do Trapezio                     !')
print ('!            D - Calculo da Area do Triangulo                    !')
opcao = str(input('!            Digite Sua opcao...: '))
print ('+================================================================+')


if (opcao == "A"):
    raio = float(input("Informe o raio do circulo.....: "))
    area = 3.1416 * (raio ** 2)

    print ("A área do círculo de raio {} é igual {} m2" .format(raio , area))
           
elif (opcao == "B"):
    base = float(input("Informe a base do retangulo.....: "))
    altura = float(input("Informe a altura do retangulo...: "))
    area = base * altura

    print ("A área do retangulo de altura {}, de base {} é igual {} m2" .format(altura, base, area))

elif (opcao == "C"):
    base_menor = float(input("Informe a base menor do trapézio.....: "))
    base_maior = float(input("Informe a base maior do trapézio.....: "))
    altura = float(input("Informe a altura do trapézio.........: "))
    area = ((base_menor + base_maior) * altura) / 2

    print ("A área do trapázio que tem base maior {}, base menor {} e altura {} é igual {} m2" .format(base_maior, base_menor, altura, area))

elif (opcao == "D"):
    base = float(input("Informe a base do triangulo......: "))
    altura = float(input("Informe a altura do triangulo....: "))
    area = (base * altura) / 2

    print ("A área do triangulo de base {}, de altura {} é igual {} m2" .format(base, altura, area))

else:
    print ("Opção invalida")
