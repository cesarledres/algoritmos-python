# Estrutura de decisão ELIF:

# Quando usar
    # Quando tivermos, no mínimo, 3 situações

# Exemplo 1: verificar se um numero é positivo, negativo ou neutro

numero = int(input("Informe um numero: "))

if numero > 0:
    print("O numero é positivo")
elif numero == 0:
    print("O numero é neutro")
else:
    print("O numero é negativo")