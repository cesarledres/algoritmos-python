'''
O dono de uma mercearia da zona rural do interior de SP necessita automatizar o processo de totalização
das compras de seus clientes, porém ele não tem condições financeiras para adquirir os equipamentos
necessários para leitura de códigos de barras e afins. Dessa forma, o funcionário do caixa terá que
digitar os preços dos produtos e as quantidades para que as compras dos clientes sejam totalizadas. 
Escreva um programa que calcule o total da compra do cliente, sendo que o usuário deverá digitar os preços
e as quantidades dos produtos e, quando a compra terminar, digitar 0 (zero) no valor do preço para
finalizar e informar o valor a pagar ao cliente.
'''

valor_total = 0
preco = 1

while preco != 0:
    preco = float(input("Digite o preço do produto (0 para sair): "))
    if preco != 0:
        qtd = int(input("Digite a quantidade do produto: "))
        total_produto = preco * qtd
        valor_total += total_produto

print(f"O valor total da compra é R$ {round(valor_total, 2)}")

