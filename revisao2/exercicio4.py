'''
Escreva um programa em Python para imprimir somente os números pares de 1 a 100. Utilize a estrutura de repetição
“while”.
'''
num = 1

while num <= 100:
    if num % 2 == 0:
        print(num)
    num += 1