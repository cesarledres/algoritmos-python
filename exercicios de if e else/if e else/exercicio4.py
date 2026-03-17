'''
Um estacionamento cobra R$ 5,00 por hora porém possui um teto de cobrança máxima de R$ 35,00, independente
do número de horas. Escreva um algoritmo que pergunte ao usuário qual foi o período de permanência em
horas e escreva na tela o total a pagar.
'''

qdt_horas = int(input("Informe a quantidade de horas permanecidas: "))
qdt_minutos = float(input("Informe a quantidade de minutos permanecidos: "))

minutos_convertidos = qdt_minutos / 60
tempo_total = minutos_convertidos + qdt_horas
valor_hora = tempo_total * 5

if valor_hora > 35:
    print("O valor total é R$ 35.")
else:
    print(f"O valor total é R$ {round(valor_hora, 2)}.")