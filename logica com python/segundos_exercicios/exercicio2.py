'''
Uma revendedora de carros usados paga a seus funcionários vendedores um salário fixo por mês, mais uma
comissão também fixa para cada carro vendido e mais 5% do valor das vendas por ele efetuadas. Escrever
um algoritmo que solicite o número de carros por ele vendidos, o valor total de suas vendas, o salário
fixo e o valor que ele recebe por carro vendido. Calcule e escreva o salário final do vendedor.
'''

salario_fixo = float(input("Informe o valor do salário fixo: "))

comissao_por_carro = float(input("Informe o valor da comissão ganhada por cada carro vendido: "))

qtd_carros_vendidos = float(input("Informe a quantidade de carros vendidos: "))

valor_carros_vendidos = float(round(comissao_por_carro * qtd_carros_vendidos, 2))

valor_total_vendas = float(input("Infome o valor total das vendas: "))

percentual_vendas = float(round(valor_total_vendas * 0.05, 2))

receita_total = float(round(salario_fixo + valor_carros_vendidos + percentual_vendas))

print(f"O valor total da receita é de R$ {receita_total}")