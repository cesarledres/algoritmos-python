'''
Um condomínio possui 4 blocos que são abastecidos por duas caixas d’água diferentes. A caixa A abastece
os blocos pares e a caixa B abastece os blocos ímpares. Escreva um algoritmo que pergunte ao usuário
em qual bloco ele mora (1-4) e escreva na tela qual a caixa que abastece seu bloco: a caixa a ou a caixa B.
'''

bloco_usuario = int(input("Informe o número do bloco que você mora: "))

resto_divisao = bloco_usuario % 2

if bloco_usuario >= 1 and bloco_usuario <= 4:
    if resto_divisao == 0: 
        print("A caixa de água que abastece o seu bloco é a A.")
    else:
        print("A caixa de água que abastece o seu bloco é a B.")
else:
    print("O bloco não pertence ao condomínio.")