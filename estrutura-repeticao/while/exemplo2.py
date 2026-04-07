# Exemplo 2: Calcular e exibir a soma de numeros positivos digite um numero negativo

# não tera contador, mas tera uma variavel para somatorio

soma_positivos = 0

num = int(input("Digite um numero inteiro (negativo para sair): "))

while num >= 0:
    soma_positivos = soma_positivos + num
    num = int(input("Digite um numero inteiro (negativo para sair): "))

print(f"A soma dos numeros positivos digitados é {soma_positivos}")