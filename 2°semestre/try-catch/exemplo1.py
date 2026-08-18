#tratamento de erros 

#sem tratamento
'''
num1 = int(input("Digite o primeiro numero inteiro: "))
num2 = int(input("Digite o segundo numero inteiro: "))

soma= num1 + num2

print(f"A soma dos dois numeros é {soma}")
'''

#com tratamento

try:
    num1 = int(input("Digite o primeiro numero inteiro: "))
    num2 = int(input("Digite o segundo numero inteiro: "))

    soma= num1 + num2

    print(f"A soma dos dois numeros é {soma}")
except ValueError: #quando da erro
    print("Os dados devem ser numericos")

else: #quando da certo
    print(f"A soma dos dois numeros é {soma}")

finally:
    print("Programa finalizado")