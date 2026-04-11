'''Desenvolva um programa que solicite ao usuário números positivos até que o valor 0 seja pressionado. 
Em seguida, calcule e exiba a média aritmética de todos os números recebidos (exceto o número 0).'''

resp = 1
soma = 0
cont = 0

while resp == 1:
    num = float(input("digite um numero (0 para sair): "))
    if num == 0:
        resp = 0
    else:
        soma += num
        cont += 1

media = soma / cont

print(f"A média dos numeros informados é {media}")