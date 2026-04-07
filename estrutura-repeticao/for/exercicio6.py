'''
Escreva um algoritmo que solicite dois números e devolva quantos pares e ímpares há entre esses dois números. Exemplo: entre 7 e 10 há 2 números pares e 2 números ímpares
'''

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

pares = 0
impares = 0

for cont in range(num1, num2+1):
    if cont % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

print(f"A quantidade de números pares é {pares}")
print(f"A quantidade de números impares é {impares}")

