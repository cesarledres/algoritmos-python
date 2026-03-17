'''
Uma livraria resolveu fazer uma promoção, com os seguintes critérios: 
- Livros com preços até R$ 10,00 - desconto de 8% 
- Livros com preços de R$ 10,01 até R$ 60,00 - desconto de 10% 
- Livros com preços acima de R$ 60,00 - desconto de 20% 
Escreva um algoritmo que leia o preço do livro e mostre o valor do desconto oferecido, em reais.
'''

preco_livro = float(input("Informe o preço do livro comprado: "))

if preco_livro > 0:
    if preco_livro <= 10:
        desconto = preco_livro * 0.08
    elif preco_livro <= 60:
        desconto = preco_livro * 0.10
    else:
        desconto = preco_livro * 0.20

    print(f"O desconto do livro foi de R$ {round(desconto, 2)}.")
else:
    print("Valor não identificado.")