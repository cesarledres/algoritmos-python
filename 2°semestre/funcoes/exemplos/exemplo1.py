# Função para exibir uma mensagem na tela

def exibir_mensagem():
    print("Fução para exibir mensagem")

# Chamada da função
exibir_mensagem()

# Função para exibir uma mensagem específica na tela

def exibir_mensagem_custom(mensagem):
    print(mensagem)

# Chamada da função
'''
mensagem = input("Digite a mensagem que quer exibir: ")
exibir_mensagem_custom(mensagem)
'''

# Função que retorna algum dado

def soma_numeros(num1, num2):
    soma = num1 + num2
    return soma

# Chamada da função
'''
num1 = int(input("Digite o primeiro numero para somar: "))
num2 = int(input("Digite o segundo numero para somar: "))

print(f"A soma dos dois números é: {soma_numeros(num1, num2)}")
'''