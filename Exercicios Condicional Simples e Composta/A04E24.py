# Autor.....: Rodney Carneiro
# Data......: 18/04/2022
# Objetivo..: Condicionais Simples e Complexas
"""
Numa empresa, cada funcionário recebe mensalmente o ordenado mais um prêmio referente a comissões.
 São dados os seguintes valores: 
    . salário bruto e prêmio, além dos valores da base do INSS, base do imposto de renda e 
      respectivas taxas ( INSS e IR). 
Deseja-se emitir o demonstrativo de pagamento de um funcionário, contendo os valores do salário bruto,
prêmio, rendimento, desconto de IR e INSS e salário líquido. 
O rendimento do funcionário é a soma do sal. bruto com o prêmio, o desconto do INSS somente incide
se o rendimento for maior do que a base do INSS e o desconto do imposto de renda somente se a 
diferença entre os valores do rendimento e o valor do desconto do INSS for maior do que a 
base do IR. 
"""

salario_bruto = float(input("Informe o salário bruto.................: "))
premio = float(input("Informe o valor do prêmio...............: "))
base_inss = float(input("Informe a base do INSS..................: "))
base_imposto = float(input("Informe a base do imposto de renda......: "))
ir = float(input("Informe as taxas do INSS................: "))
inss = float(input("Informe as taxas do IR..................: "))

rendimento = salario_bruto + premio

if(rendimento > base_inss):
    valor_inss = (rendimento * (inss/100))
    rendimento = rendimento - valor_inss
else:
    valor_inss = 0

if(rendimento > base_imposto):
    valor_ir = (rendimento * (ir/100))
    rendimento = rendimento - valor_ir
else:
    valor_ir = 0

#--- Saidas
print(" - Salario Bruto é de R$ {salario_bruto:.2f}")
print(" - O valor do Premio é de R$ {premio:.2f}")
print(" - O valor de Desconto do Inss é R$ {valor_inss:.2f}")
print(" - O valor de desconto do Imposto de Renda é de R$ {valor_ir:.2f}")
print(" - O valor Liquido a ser recebido é de R$ {rendimento:.2f}")
