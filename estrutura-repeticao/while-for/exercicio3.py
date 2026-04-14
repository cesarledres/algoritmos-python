'''Mostrar todos os inteiros entre dois números digitados pelo usuário. Exemplo: usuário digita os números
8 e 15, e aparecem em tela: 9, 10, 11, 12, 13, 14.'''

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

cont = num1 + 1

while cont < num2:
    print(cont)
    cont += 1