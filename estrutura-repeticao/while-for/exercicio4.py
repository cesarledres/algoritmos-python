'''
Faça um programa que verifique se uma "senha” numérica digitada pelo usuário está correta. O programa deve
repetir o pedido até que o usuário escreva o valor correto. A senha correta deve estar definida no próprio
programa.
'''

senha = 14052007
tentativa = 0

while tentativa != senha:
    tentativa = int(input("Digite a senha: "))
    if tentativa == senha:
        print("Senha correta")
    else:
        print("Senha incorreta")