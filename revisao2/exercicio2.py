'''
Faça um programa em Python que solicite ao usuário o valor de n e que mostre os n termos da Série a seguir:
S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
Nesse caso, utilize a estrutura de repetição “for”.
'''

numerador = 0
denominador = -1
serie = 0

n = int(input("Digite um número inteiro: "))

for i in range(n):
    numerador += 1
    denominador += 2
    print()

# pulei


