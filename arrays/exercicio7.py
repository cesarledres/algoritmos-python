'''
Escreva um programa que simule um dicionário inglês/português utilizando o conceito de listas. Para tanto,
crie uma lista para as palavras em inglês e outra para as traduções em português nas respectivas posições.
A inserção das palavras deverá ser executada até que o usuário digite uma opção de saída 0 (Deseja
continuar (1-SIM / 0-NÃO). Após a inserção, exiba a tradução em português de uma determinada palavra em
inglês que o usuário deverá digitar.
'''

dicionario_portugues = []
dicionario_ingles = []
resposta = 1

while resposta != 0:
    palavra_portugues = input("Digite uma palavra em português: ")
    dicionario_portugues.append(palavra_portugues)

    palavra_ingles = input("Digite a traducção em inglês dessa palavra: ")
    dicionario_ingles.append(palavra_ingles)

    resposta = int(input("Deseja continuar? [1-SIM / 0-NÃO]: "))

resposta = 1

while resposta != 0:
    palavra_ingles_usuario = input("Digite uma palavra em inglês que esteja no dicionário: ")
    
    if palavra_ingles_usuario in dicionario_ingles:
        for i in dicionario_ingles:
            if palavra_ingles_usuario == i:
                indice_palavra_ingles_usuario = dicionario_ingles.index(i)
                indice_palavra_portugues_usuario = indice_palavra_ingles_usuario

        print(f"A tradução da palavra digitada é: {dicionario_portugues[indice_palavra_portugues_usuario]}")
    else:
        print("Palavra não encontrada no dicionário.")
    
    resposta = int(input("Deseja continuar? [1-SIM / 0-NÃO]: "))

# fazer menu (match case)