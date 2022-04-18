# Autor.....: Rodney Carneiro
# Data......: 17/04/2022
#Objetivo...: 
"""
Escreva um algoritmo para criar um programa de ajuda para vendedores. A partir de um valor total
recebido do teclado, mostrar:
. o total a pagar com desconto de 10%;
. o valor de cada parcela, no parcelamento de 3 x sem juros;
. a comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto )
. a comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total)
 
"""
#---- Programa Principal

#---- Entradas
valor=float(input("Digite o Valor Total...: "))

#---- Processamento
total_desconto = valor - (valor * (10 / 100))
valor_parcelas = valor / 3
comissao_avista = total_desconto * (5/100)
comissao_aprazo = valor * (5 / 100)

#---- Saidas
print(f"O Valor com Desconto de 10% é R$ {total_desconto:.2f}")
print(f"O Valor da Parcela sera de R$ {valor_parcelas:.2f}")
print(f"Comissao do Vendedor para venda a Vista R$ {comissao_avista:.2f}")
print(f"Comissao do vendedor para venda a Prazo R$ {comissao_aprazo:.2f}")