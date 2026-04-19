'''
A prefeitura de uma cidade deseja fazer uma pesquisa entre seus habitantes. Escreva um programa em Python para coletar
dados sobre o salário e número de filhos de cada habitante e após as leituras, escrever:
a) Média de salário da população
b) Média do número de filhos
c) Maior salário dos habitantes
d) Percentual de pessoas com salário menor que R$ 150,00
Obs.: O final das leituras dos dados se dará com a entrada de um “salário negativo”. Utilize a estrutura de repetição
“while”.
'''
salario = 0
soma_salario = 0
soma_filhos = 0
maior_salario = 0
indice_cadastramento = 0
qtd_pessoas_menos_150 = 0

while salario >= 0:
    salario = float(input("Digite o salário (negativo para sair): "))
    if salario >= 0:
        num_filhos = int(input("Digite o número de filhos: "))
        indice_cadastramento += 1

        soma_salario += salario

        soma_filhos += num_filhos

        if salario > maior_salario:
            maior_salario = salario

        if salario < 150:
            qtd_pessoas_menos_150 += 1

media_salario = soma_salario / indice_cadastramento
media_filhos = soma_filhos / indice_cadastramento
perc_pessoas_menos_150 = qtd_pessoas_menos_150 / indice_cadastramento * 100

print(f"Média salarial: {round(media_salario, 2)}")
print(f"Média de filhos p/ pessoa: {round(media_filhos)}")
print(f"Maior salário: {maior_salario}")
print(f"Percentual de pessoas com salário menor que R$ 150,00: {round(perc_pessoas_menos_150, 1)}%")