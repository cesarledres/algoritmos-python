'''
Escreva um programa em Python que crie uma lista de 7 dicionários, a qual deve conter os seguintes dados: 

Matrícula (inteiro); 
Nome (string);] 
Plano (string, ex: "Anual", "Mensal") 
Modalidade (string, ex: "Musculação", "Crossfit") 
Presenças no Mês 

Em seguida, exiba todos os alunos da academia. 
'''

lista_alunos = []

for i in range(2):
    matricula = int(input("Digite a matricula: "))
    nome = input("Digite o nome: ")
    plano = input("Digite o plano: ")
    modalidade = input("Digite a modalidade: ")
    presencas = int(input("Digite a quantidade de presenças no mês: "))

    dados_alunos = {
        'matricula': matricula,
        'nome': nome,
        'plano': plano,
        'modalidade': modalidade,
        'presencas': presencas
    }

    lista_alunos.append(dados_alunos)

for i in range(len(lista_alunos)):
    for chave, valor in lista_alunos[i].items():
        print(f"{chave}:{valor}")
    print("----------------")