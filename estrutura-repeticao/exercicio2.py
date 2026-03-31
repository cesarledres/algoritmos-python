'''
Faça um programa que receba 5 números inteiros e mostre se ele é par ou ímpar, um a um. Ou seja, conforme
o usuário digita o número seu programa deverá informar se o número digitado é par ou ímpar.
'''

for cont in range(5):
    num = int(input("Digite um número inteiro para verificar se é par ou impar: "))

    if num % 2 == 0:
        print(f"{num} é par")
    else:
        print(f"{num} é impar")