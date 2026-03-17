'''
Escreva um programa que pergunte em qual mês estamos (1-12) e ao final utilize uma estrutura de decisão
por seleção para escrever o nome do mês por extenso na tela.
'''

mes = int(input("Informe número do mês: "))

if mes == 1:
    print("O mês é Janeiro.")
elif mes == 2:
    print("O mês é Fevereiro.")
elif mes == 3:
    print("O mês é Março.")
elif mes == 4:
    print("O mês é Abril.")
elif mes == 5:
    print("O mês é Maio.")
elif mes == 6:
    print("O mês é Junho.")
elif mes == 7:
    print("O mês é Julho.")
elif mes == 8:
    print("O mês é Agosto.")
elif mes == 9:
    print("O mês é Setembro.")
elif mes == 10:
    print("O mês é Outubro.")
elif mes == 11:
    print("O mês é Novembro.")
elif mes == 12:
    print("O mês é Dezembro.")
else:
    print("Mês não identificado.")