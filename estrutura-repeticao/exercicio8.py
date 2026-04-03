'''
•	Desenvolva um programa que receba:
o	taxa de abatimento em porcentagem;
o	número de prestações;
o	valor da primeira prestação.
Seu programa deverá exibir na tela os valores das prestações decrescente dado que a cada mês o valor da
prestação diminui do valor da prestação do mês anterior (utilize a taxa de abatimento fornecida pelo
usuário para realizar esse cálculo). OBS: utilize o “for”.
'''

taxa_abatimento = int(input("Informe em porcentagem a taxa de abatimento: "))
numero_prestacoes = int(input("Informe o número de prestações: "))
prestacao = float(input("Informe o valor da primeira prestação: "))

print("Prestações a pagar:")

for cont in range(numero_prestacoes):
    print(f"R$ {round(prestacao, 2)}")
    prestacao = prestacao * ((100 - taxa_abatimento) / 100)