'''
Baseado em um número real X (float) digitado pelo usuário, utilize o desvio condicional de múltipla escolha e faça as seguintes operações:

Opcao = 1: adicione 5 ao valor de X e exiba na tela.
Opcao = 2: subtraia 4 ao valor de X e exiba na tela.
Opcao = 3: dobre o valor de X e exiba na tela.
'''

print("---------- MENU DE OPÇÕES ----------")
print("1) Adicione 5 ao número inserido.")
print("2) Subtraia 4 ao número inserido.")
print("3) Dobre o valor inserido.")

opcao = int(input("Digite o número da sua opção: "))
numero = float(input("Digite um número: "))

match opcao:
    case 1:
        numero_final = numero + 5
        print(numero_final)
    case 2:
        numero_final = numero - 4
        print(numero_final)
    case 3:
        numero_final = numero * 2
        print(numero_final)
    case _:
        print("Opção não válida.")