'''
uma função que tenha um parâmetro “n” e que calcule e retorne a média de todos os
pares de 1 até N.
'''

def calcula_media(n):
    soma_pares = 0
    qtd_pares = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            soma_pares += i
            qtd_pares += 1
    media_pares = soma_pares / qtd_pares
    return media_pares

num = int(input("Digite um numero: "))

media = calcula_media(num)

print(f"A média dos pares de 1 até o número informado é {media}")