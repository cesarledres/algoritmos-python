'''
Escreva um algoritmo que pergunte o valor de uma mercadoria e qual o valor que o usuário tem em mãos
e diga se o dinheiro é ou não é suficiente para adquirir esta mercadoria.
'''

valor_mercadoria = float(input("Informe o valor da mercadoria: "))
valor_usuario = float(input("Informe o quanto de dinheiro você tem: "))

if valor_usuario >= valor_mercadoria:
    print("É possível comprar.")
else:
    print("Não é possível comprar.")