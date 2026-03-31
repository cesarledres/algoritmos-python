# exemplo4 4: somar 10 numeros digitados pelo usuario

soma = 0

for cont in range(10): # inicio vai ser 0 e o fim 9
    num = int(input("Informe um numero: "))
    soma = soma + num

print(f"O total da soma é {soma}")