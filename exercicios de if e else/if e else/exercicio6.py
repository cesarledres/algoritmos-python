'''
As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo
menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da
compra.
'''

qdt_macas_compradas = int(input("Informe a quantidade de maças compradas: "))

if qdt_macas_compradas < 12:
    valor_maca1 = qdt_macas_compradas * 1.3
    print(f"O valor total das maçãs é R$ {round(valor_maca1, 2)}")
else:
    valor_maca2 = qdt_macas_compradas # apenas para entendimento
    print(f"O valor total das maçãs é R$ {valor_maca2}")



# calcular a variave no else e mostrar o print fora
'''
if qdt_macas_compradas < 12:
    valor_maca = qdt_macas_compradas * 1.3
else:
    valor_maca = qdt_macas_compradas

    print(f"O valor total das maçãs é R$ {roundo(valor_maca, 2)}")
'''