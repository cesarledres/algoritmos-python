'''
●	Escreva um programa que contenha o seguinte menu:
Opção 1: Verificar e exibir se um número x é ou não divisível por 6;
Opção 2: Calcular o fatorial do número x;
Opção 3: Exibir todos os inteiros de 1 até um número x.
O programa deverá solicitar ao usuário a leitura de um número x e a opção desejada até que o usuário
digite “N” para encerrar o programa. OBS: o programa deverá solicitar o número e a opção enquanto do
usuário escolha “S”.
'''

resp = 0
produtorio = 1

while resp != "N" and resp != "n":
    print("MENU DE OPÇÕES")
    print("1) Verificar e exibir se um número x é ou não divisível por 6.")
    print("2) Calcular o fatorial do número x.")
    print("3) Exibir todos os inteiros de 1 até um número x.")

    opcao = int(input("Digite a opcão desejada: "))
    
    if opcao >= 1 and opcao <= 3:
        x = int(input("Digite um numero inteiro: "))

        if x >= 0:
            match opcao:
                case 1:
                    if x % 6 == 0:
                        print("O número é divível por 6.")
                    else:
                        print("O número não é divível por 6.")
                case 2:
                    for cont in range(1, x+1):
                        produtorio *= cont
                    print(f"O fatorial desse número é {produtorio}")
                case 3:
                    for cont in range(1, x+1):
                        print(cont)
        else:
            print("Número inválido.")
    else:
        print("Opção inválida.")
    
    resp = input("Deseja continuar? ([S] Sim / [N] Não): ")
            