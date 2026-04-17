'''
Faça um programa em Python que peça as 3 notas de 10 alunos, calcule e armazene em uma lista a média de
cada aluno. Em seguida, imprima o número de alunos com média maior ou igual a 7.0.
'''
lista_media = []
alunos_nota7 = 0

for i in range(10):
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    media = (nota1 + nota2 + nota3) / 3

    lista_media.append(round(media, 1))

    if media >= 7:
        alunos_nota7 =+ 1

print(f"O número de alunos com média maior ou igual a 7: {alunos_nota7}")