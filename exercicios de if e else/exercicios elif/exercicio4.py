'''
Considerando o IMC (índice de massa corpórea), calculado como peso/(altura*altura), exiba a situação da
pessoa com base na seguinte tabela:

|IMC	        |Situação      |
|---------------|--------------|
|<= 18.5	    |Abaixo do peso|
|>18.5 e <=24.9	|Peso ideal    |
|>24.9	        |Acima do peso |
'''
# entrada de dados da altura e peso
peso = float(input("Informe o peso: "))
altura = float(input("Informe a altura: "))

# validação peso e altura
if peso <= 0:
    print("Peso inválido.")
elif altura <= 0:
    print("Altura inválida.")

# calculo e visualização do imc
else:
    imc = peso / altura**2
    print(f"Seu IMC é {round(imc, 2)}.")

# identifica nivel de peso com base no valor do imc
    if imc <= 18.5:
        print("Abaixo do peso.")
    elif imc <= 24.9:
        print("Peso ideal.")
    else:
        print("Acima do peso.")



