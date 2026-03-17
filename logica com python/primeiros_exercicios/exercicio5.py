from wsgiref.validate import validator


valor_cotacao = 5.24
valor_dolares = float(input(f"Informe o valor em dolares: "))

valor_reais = float(round(valor_dolares * valor_cotacao, 2))

print(f"O valor convertido para real é: R$ {valor_reais}")