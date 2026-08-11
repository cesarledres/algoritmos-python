'''
Uma função com dois parâmetros (a e b) que mostre o maior deles;
'''

def mostrar_maior_numero(a, b):
    if a > b:
        return a
    return b

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

print(f"O maior número entre os dois é: {mostrar_maior_numero(num1, num2)}")
