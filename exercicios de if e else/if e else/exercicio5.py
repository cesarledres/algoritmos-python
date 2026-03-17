'''
Escreva um algoritmo que verifique se um número inteiro digitado pelo usuário é ou não divisível por 5.
'''

valor_usuario = int(input("Informe um valor para verificar se é ou divisível por 5: "))

resto_divisao = valor_usuario % 5

if resto_divisao == 0:
    print("Este valor é divisivel por 5.")
else:
    print("Esta valor não é divisivel por 5.")