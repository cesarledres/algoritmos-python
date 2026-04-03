'''
Escreva um programa que calcule o somatório de todos os números pares em um intervalo definido pelo
usuário. Ex: para inicio = 2 e fim = 10 o somatório é 2+4+6+8+10. OBS: utilize o “for”.
'''

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

soma_pares = 0

for cont in range(num1, num2+1):
    if cont % 2 == 0:
        soma_pares += cont
    
print(f"A soma de todos os números pares é {soma_pares}")

