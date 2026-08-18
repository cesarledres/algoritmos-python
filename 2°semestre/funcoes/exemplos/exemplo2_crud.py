def main():
    lista_clientes = []
    opcao = 1

    while opcao != 6:
        print("1 - Inserir cliente")
        print("2 - Alterar cliente")
        print("3 - Excluir cliente")
        print("4 - Exibir dados de um cliente")
        print("5 - Exibir os clientes com saldo acima de 10k")
        print("6 - Sair")

        opcao = int(input("Digite a opcao desejada (1 a 6): "))
        if opcao >= 1 and opcao <= 6:
            match opcao:
                case 1:
                    inserir_cliente(lista_clientes)
                case 2:
                    codigo_alterar = int(input("Digite o código do cliente que deseja alterar: "))
                    indice = buscar_cliente(lista_clientes, codigo_alterar)
                    if indice != -1:
                        alterar_cliente(lista_clientes, indice)
                    else:
                        print("Codigo não encontrado")
                case 3:
                    codigo_alterar = int(input("Digite o código do cliente que deseja excluir: "))
                    indice = buscar_cliente(lista_clientes, codigo_alterar)
                    if indice != -1:
                        excluir_dados_cliente(lista_clientes, indice)
                    else:
                        print("Codigo não encontrado")
                case 4:
                    codigo_alterar = int(input("Digite o código do cliente que deseja exibir os dados: "))
                    indice = buscar_cliente(lista_clientes, codigo_alterar)
                    if indice != -1:
                        exibir_dados_cliente(lista_clientes, indice)
                    else:
                        print("Codigo não encontrado")
                case 5:
                    exibir_clientes_acima_10k(lista_clientes)
        else:
            print("Opção inválida")

# Funções do CRUD
def inserir_cliente(lista_clientes):
    codigo_cliente = int(input("Digite o código do cliente: "))
    nome_cliente = input("Digite o nome do cliente: ")
    nro_agencia = int(input("Digite o numero da agencia do cliente: "))
    nro_conta_corrente = int(input("Digite o numeor da conta corrente do cliente: "))
    saldo_cleinte = float((input("Digite o saldo do cliente: ")))

    dados_cliente = {
        'Codigo_cliente': codigo_cliente,
        'Nome_cliente': nome_cliente,
        'Nro_agencia': nro_agencia,
        'Nro_conta_corrente': nro_conta_corrente,
        'Saldo_cliente': saldo_cleinte
    }

    lista_clientes.append(dados_cliente)

def buscar_cliente(lista_clientes, codigo):
    #primeiro indice da lista é 0
    indice = -1
    for i in range(len(lista_clientes)):
        if codigo == lista_clientes[i]['Codigo_cliente']:
            indice = i
    return indice

def alterar_cliente(lista_clientes, indice):
    print(f"Nome do cliente: {lista_clientes[indice]['Nome_cliente']}")
    novo_cliente = input("Digite o novo nome do cliente: ")
    
    print(f"Numero da agencia: {lista_clientes[indice]['Nro_agencia']}")
    novo_numero_agencia = int(input("Digite o novo numero da agencia do cliente: "))
    
    print(f"Numero da conta corrente do cliente: {lista_clientes[indice]['Nro_conta_corrente']}")
    novo_numero_conta_corrente = int(input("Digite o novo numero da conta corrente: "))

    print(f"Saldo do cliente: {lista_clientes[indice]['Saldo_cliente']}")
    novo_saldo_cliente = float(input("Digite o novo saldo do cliente: "))

    lista_clientes[indice]['Nome_cliente'] = novo_cliente
    lista_clientes[indice]['Nro_agencia'] = novo_numero_agencia
    lista_clientes[indice]['Nro_conta_corrente'] = novo_numero_conta_corrente
    lista_clientes[indice]['Saldo_cliente'] = novo_saldo_cliente

def excluir_dados_cliente(lista_clientes, indice):
    lista_clientes.pop(indice)

def exibir_dados_cliente(lista_clientes, indice):
    for chave, valor in lista_clientes[indice].items():
        print(f"{chave}:{valor}")

def exibir_clientes_acima_10k(lista_clientes):
    for i in range(len(lista_clientes)):
        if(lista_clientes[i]['Saldo_cliente'] > 10000):
            for chave, valor in lista_clientes[i].items():
                print(f"{chave}:{valor}")
        print("------------------------")

if __name__ == "__main__":
    main()