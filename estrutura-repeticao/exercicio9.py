'''
Escreva um programa para calcular o fatorial de um número n digitado pelo usuário. 
Por exemplo: n = 5     fatorial = 5 x 4 x 3 x 2 x 1 = 120. OBS: utilize o “for”.
'''

n = int(input("Digite um número para calcular o fatorial deste: "))

if n < 0:
    print("Fatorial indefinido.")
else:
    fatorial = 1
    for cont in range(1, n+1):
        fatorial *= cont #boa pratica

print(f"O fatorial deste número é {fatorial}")
        