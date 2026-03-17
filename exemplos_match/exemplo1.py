# Estrutura de Decisão match...case

# Exemplo 1: solicitar 2 numeros inteiros e uma opção para o usuario escolher qual operação quer executar (adição, subtração, multiplicação ou divisão)

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

print("---------- MENU DE OPÇÕES -----------")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = int(input("Digite a opção desejada (1 a 4): "))

match opcao:
    case 1:
        soma = num1 + num2
        print(f"O resultado da soma é {soma}.")
    case 2:
        subtracao = num1 - num2
        print(f"O resultado da subtração é {subtracao}.")
    case 3:
        mult = num1 * num2
        print(f"O resultado da multiplicação é {mult}.")
    case 4:
        div = num1 / num2
        print(f"O resultado da divisão é {round(div)}.")
    case _:
        print("Opção inválida.")