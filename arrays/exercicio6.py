'''
Desenvolva um programa que recebe 10 números inteiros e os armazene em uma lista. Em seguida, exiba
quantos números múltiplos de 3 ela possui.
'''
lista = []
lista_multiplos_de_3 = []

for i in range(10):
    num = int(input("Digite um número inteiro: "))
    lista.append(num)

for i in lista:
    if i % 3 == 0:
        lista_multiplos_de_3.append(i)

qtd_multiplos_de_3 = len(lista_multiplos_de_3)

print(f"A quantidade de números inteiros multiplos de 3 na lista: {qtd_multiplos_de_3}")