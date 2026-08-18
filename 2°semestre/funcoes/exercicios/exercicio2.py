'''
Uma função com um parâmetro x que calcule e mostre o dobro de x.
'''

def calcula_dobro(x):
    return x * 2

num = int(input("Digite um numero para calcular o dobro: "))

print(f"O dobro do numero informado é: {calcula_dobro(num)}")