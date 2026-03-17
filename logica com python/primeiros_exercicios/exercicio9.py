qnd_hora = float(input("Informe a quantidade de horas: "))
qnd_minutos = float(input("Infome a quantidade de minutos: "))

valor_hora = float(qnd_hora * 5)
valor_minuto = float(round((qnd_minutos / 60) * 5, 2))
valor_total = float(valor_minuto + valor_hora)

print(f"O o total do valor por hora é {valor_total}")