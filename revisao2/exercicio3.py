'''
Numa eleição existem três candidatos. Faça um programa em Python que solicite ao usuário o número total de eleitores.
Em seguida, peça para cada eleitor votar e ao final mostre o número de votos de cada candidato. Nesse caso, utilize a
estrutura de repetição “for”.
'''

total_eleitores = int(input("Digite o número total de eleitores: "))
candidatoA = 0
candidatoB = 0
candidatoC = 0

for i in range(total_eleitores):
    numero_candidato = int(input("Digite o número do cantidado que quer votar (1 a 3): "))
    if numero_candidato >= 1 and numero_candidato <= 3:
        if numero_candidato == 1:
            candidatoA += 1
        elif numero_candidato == 2:
            candidatoB += 1
        elif numero_candidato == 3:
            candidatoC += 1
    else:
        while numero_candidato < 1 or numero_candidato > 3:
            numero_candidato = int(input("Número inválido. Digite novamente (1 a 3): "))
            if numero_candidato == 1:
                candidatoA += 1
            elif numero_candidato == 2:
                candidatoB += 1
            elif numero_candidato == 3:
                candidatoC += 1

print(f"O número de votos do candidato A é {candidatoA}")
print(f"O número de votos do candidato B é {candidatoB}")
print(f"O número de votos do candidato C é {candidatoC}")