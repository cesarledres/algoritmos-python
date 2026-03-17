altura = float(input("Informe a altura: "))
peso = float(input("Informe o peso: "))

imc = float(peso / (altura**2))

print(f"O IMC é {round(imc, 2)}")