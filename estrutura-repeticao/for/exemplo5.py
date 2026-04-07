# exemplo 5: calcular e exibir as medias de 3 avaliações para 5 alunos

for cont in range(5):
    av1 = float(input("Digite a nota da primeira avaliação: "))
    av2 = float(input("Digite a nota da segunda avaliação: "))
    av3 = float(input("Digite a nota da terceira avaliação: "))
    media = (av1 + av2 + av3) / 3

    print(f"A média do aluno é {round(media, 2)}")