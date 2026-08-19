'''
Escreva um programa em Python que realize um CRUD em uma lista de
dicionários, a qual deve conter os seguintes dados: 

Matrícula; 
Nome; 
Plano (ex: "Anual", "Mensal") 
Modalidade (ex: "Musculação", "Crossfit") 
Presenças no Mês. 

O programa deverá ter uma estrutura de menu para as operações do CRUD
(inserção, alteração, exclusão e exibição dos dados). Faça os tratamentos
de erros na inserção e alteração.  Além disso, faça a validação de 
unicidade para simular a matrícula como chave primária.
'''

def main():
    lista_clientes = []

    opcao = 1

    while opcao != 5:
        print("1 - Inserir cliente")
        print("2 - Alterar cliente")
        print("3 - Excluir cliente")
        print("4 - Exibir cliente")
        print("5 - Sair")
        
        opcao = int(input("Digite a opção desejada: "))

def buscar_cliente(lista_clientes, matricula):
    indice = -1
    for i in lista_clientes:
        if matricula == lista_clientes[i]['Matricula']:
            indice = i
            return indice

def inserir_cliente(lista_clientes):
    try:
        matricula = int(input("Digite a matrícula do cliente: "))
        indice = buscar_cliente(lista_clientes, matricula)
        while indice != -1:
            matricula = int(input("Está matriácula já existe, digite outra: "))
            buscar_cliente(lista_clientes, matricula)
        
        nome = input("Digite o nome do cliente: ")
        plano = input("Digite o plano do cliente: ")
        modalidade = input("Digite a modalidade do cliente: ")
        presenca = int(input("Digite a quantidade de presenças no mês: "))
    except ValueError:
        print("Digite dados númericos para os campos de matricula e prenseça.")
    else:
        dados_cliente = {
            'Matricula': matricula,
            'Nome': nome,
            'Plano': plano,
            'Modalidade': modalidade,
            'Presenca': presenca
        }

        lista_clientes.append(dados_cliente)
        print("Cliente cadastrado com sucesso!")

def alterar_cliente(lista_clientes, indice):
    