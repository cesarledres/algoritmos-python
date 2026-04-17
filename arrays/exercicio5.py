'''
Desenvolva um programa que preencha um vetor com as idades dos usuários até que o usuário digite um valor
negativo, o valor negativo não deve ser inserido na lista. Ao final, exiba na tela:
- A quantidade de usuários menores de 18 anos; 
- A média das idades.
'''

idade = 0
lista_idade = []
lista_menores_18 = []

while idade >= 0:
    idade = int(input("Digite a idade (número negativo para sair): "))
    if idade >= 0:
        lista_idade.append(idade)

for i in lista_idade:
    if i < 18:
        lista_menores_18.append(i)
qtd_menores_18 = len(lista_menores_18)

soma_idade = sum(lista_idade)
qtd_idade = len(lista_idade)
media_idade = soma_idade / qtd_idade

print(f"A quantidade de menores de 18 anos é {qtd_menores_18}")
print(f"A média das idades é {round(media_idade, 2)}")
print(lista_menores_18)