'''Desenvolva um programa que recebe as notas dos alunos de uma turma. Seu programa deverá ser
interrompido quando uma nota negativa for digitada.
Durante o processamento seu programa deverá contar o número de alunos nas seguintes condições:
 - média abaixo de 3.5 (reprovados direto)
 - média entre 3,5 e 7 (exame)
 - acima de 7 (aprovados)
Calcule a média aritmética da turma e informe o resultado no final.
Além disso, exiba na tela a quantidade de alunos aprovados, reprovados e exame.'''

nota = 1
alunos_abaixo = 0
alunos_media = 0
alunos_acima = 0
soma = 0
cont = 0

while nota > 0:
    nota = float(input("Digite a nota do aluno de 0 a 10 (negativo para sair): "))
    if nota >= 0 and nota <= 10:
        if nota < 3.5:
            alunos_abaixo += 1
        elif nota < 7:
            alunos_media += 1
        else:
            alunos_acima += 1
        soma = soma + nota
        cont = cont + 1
    else:
        print("Nota invalida")

media = soma / cont
print(f"A média da turma é {media}")
print(f"A quantidade de alunos abaixo da média é {alunos_abaixo}")
print(f"A quantidade de alunos na média é {alunos_media}")
print(f"A quantidade de alunos acima da média é {alunos_acima}")
