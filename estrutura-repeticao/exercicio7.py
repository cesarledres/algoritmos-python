'''
•	Desenvolva um programa para calcular a média salarial dos funcionários da empresa XXX, para isso seu
programa deverá solicitar o nome e salário dos 5 funcionários que trabalham nessa empresa. Ao final seu
programa deverá calcular a média dos salários e exibir na tela as seguintes informações:  (use 2 casas
decimais na exibição dos números)
o	A média salarial dos funcionários da empresa XXX é _______
o	O nome e o salário do funcionário que recebe o menor salário
o	O nome e o salário do funcionário que recebe o maior salário
'''

soma = 0

for cont in range(5):
    nome = input("Informe o nome do funcionário: ")
    salario = float(input("Informe o salário do funcionáio: "))

    soma = soma + salario

    if cont == 0:
        menor_salario = salario
        maior_salario = salario
        maior_nome = nome
        menor_nome = nome
    
    else:
        if salario < menor_salario:
            menor_salario = salario
            menor_nome = nome
        
        if salario > maior_salario:
            maior_salario = salario
            maior_nome = nome
    
media = soma / 5

print(f"O menor sálario é de R$ {round(menor_salario, 2)} e pertence a {menor_nome}")
print(f"O maior sálario é de R$ {round(maior_salario, 2)} e pertence a {maior_nome}")
print(f"A média de todos os salários é de R$ {round(media, 2)}")