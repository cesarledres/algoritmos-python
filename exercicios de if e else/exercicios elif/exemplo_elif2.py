# exemplo 2: verificar se um aluno esta aprovado, recuperação ou reprovado

nota = float(input("Informe a nota: "))

if nota >= 0 and nota <=10:
    if nota >= 7:
        print("Aluno aprovado.")
    elif nota >= 4:
        print("Aluno de recuperação.")
    else:
        print("Aluno reprovado.")
else:
    print("A nota não está na escala de 0 a 10.")
    