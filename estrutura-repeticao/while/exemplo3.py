# Exemplo 3: Calculadora - O usuário poderá escolher a opção que ele quiser por meio de um menu. No menu tera as opções para as 4 operações básicas. Quando o usuário quiser sair, ele devera digitar 0 (1-sim/2-nao)

resp = 1 #1 - continuar no programa e 0 - sair

while resp == 1:
    print("1 - Somar os 2 numeros")
    print("2 - Subtrair os 2 numeros")
    print("3 - Multiplicar os 2 numeros")
    print("4 - Dividir os 2 numeros")

    opcao = int(input("Digite o numero da sua opção: "))

    if opcao >= 1 and opcao <= 4:
        num1 = int(input("Digite o primeiro numero: "))
        num2 = int(input("Digite o segundo numero: "))

        match opcao:
            case 1:
                soma = num1 + num2
                print(f"A soma dos dois numeros é {soma}")
            case 2:
                subtracao = num1 - num2
                print(f"A subtração dos dois numeros é {subtracao}")
            case 3:
                multiplicacao = num1 * num2
                print(f"A multiplicação dos dois numeros é {multiplicacao}")
            case 4:
                divisao = num1 / num2
                print(f"A soma dos dois numeros é {divisao}")
    else:
        print("Opção inválida")

    resp = int(input("Deseja continuar? (1-SIM / 0-NÃO) "))





