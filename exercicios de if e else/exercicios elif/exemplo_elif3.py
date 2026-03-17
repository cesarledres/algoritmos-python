# Exemplo 3: Verificar qual é o sub da modalidade de natação por idade

idade = int(input("Informe a idade: "))

if idade >= 5 and idade <= 75:
    if idade <= 11:
        print("Seu sub é infantil.")
    elif idade <= 17:
        print("Seu sub é juvenil.")
    elif idade <= 64:
        print("Seu sub é adulto.")
    else:
        print("Seu sub é senil.")
else:
    print("Você não pode competir com essa idade.")
