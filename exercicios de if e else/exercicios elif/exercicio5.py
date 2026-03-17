'''
Uma quitanda está vendendo frutas com a seguinte tabela de preços:

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
'''

kg_morango = int(input("Informe a quantidade de morangos em quilo: "))
kg_macas = int(input("Informe a quantidade de maças em quilo: "))

if kg_morango <= 5:
    preco_morango = kg_morango * 2.5
else:
    preco_morango = kg_morango * 2.2

if kg_macas <= 5:
    preco_maca = kg_morango * 1.8
else:
    preco_maca = kg_morango * 1.5

total_kg = kg_morango + kg_macas
preco_total = preco_maca + preco_morango

if total_kg > 8 or preco_total > 25:
    preco_total = preco_total * 0.9

print(f"O total a pagar é {preco_total}.")

