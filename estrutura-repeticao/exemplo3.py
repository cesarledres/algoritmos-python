# exemplo 3: somar os numeros impares de 4 ate 100

soma_impares = 0
# zerar variavel sempre que fizer soma em estrutura de repetição / somatório

for cont in range(4,101):
    if (cont % 2 != 0):
        soma_impares = soma_impares + cont
    
print(f"A soma dos impares é {soma_impares}")
