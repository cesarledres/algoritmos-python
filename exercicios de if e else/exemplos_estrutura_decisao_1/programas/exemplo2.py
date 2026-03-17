# Exemplo 2: Verificar e exibir se um numero eh par ou impar
num = int(input("Informe um numero inteiro: "))

resto = num % 2

if (resto == 0):
    print("O numero eh PAR")
else:
    print("O numero eh IMPAR")

