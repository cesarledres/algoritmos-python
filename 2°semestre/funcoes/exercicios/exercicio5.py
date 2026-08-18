'''
uma função chamada somaImposto, que possua dois parâmetros: taxaImposto, que é a
quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de
um item antes do imposto. A função “altera” o valor de custo para incluir o imposto
sobre vendas e deve retornar o custo com o imposto.
'''

def somaImposto(taxa_imposto, custo_item):
    return (taxa_imposto + 1) * custo_item

taxa_imposto = int(input("Digite em porcentagem a taxa de imposto: "))
taxa_imposto /= 100
custo_item = float(input("Digite o custo do item: "))

custo_com_imposto = somaImposto(taxa_imposto, custo_item)

print(f"O custo com imposto somado é de R$ {round(custo_com_imposto, 2)}")