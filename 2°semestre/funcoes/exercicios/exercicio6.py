'''
uma função valorPagamento para determinar o valor a ser pago por uma prestação de
uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de
dias em atraso e passar estes valores para a função valorPagamento. O cálculo do valor
a ser pago é feito da seguinte forma: para pagamentos sem atraso, cobrar o valor da
prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de
atraso. A função deverá retornar o valor da prestação.
'''



def valor_pagamento(valor_prestacao, numero_dias):
    if numero_dias == 0:
        return valor_prestacao
    elif numero_dias > 0:
        return valor_prestacao * 1.03 + 1.001 * numero_dias

valor_prestacao = float(input("Digite o valor da pretação: "))
numero_dias = int(input("Digite o número de dias atrasados: "))

valor_final = valor_pagamento(valor_prestacao, numero_dias)

print(f"O valor final da prestação é de R$ {round(valor_final, 2)}")