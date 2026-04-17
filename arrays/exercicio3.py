'''
Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a
entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada
de dados, faça:
Mostre a quantidade de valores que foram lidos;
a.	Calcule e mostre a soma dos valores;
b.	Calcule e mostre a média dos valores;
c.	Calcule e mostre a quantidade de valores acima da média calculada;
d.	Calcule e mostre a quantidade de valores abaixo de sete.
'''

nota = 0
lista_notas_lidas = []


while nota != -1:
    nota = float(input("Digite uma nota (-1 para sair): "))
    if (nota < -1) or (nota > 10):
        print("Nota inválida.")
    elif (nota > -1 and nota < 0):
        print("Nota inválida.")
    else:
        if nota != -1:
                lista_notas_lidas.append(nota)

qtd_notas = len(lista_notas_lidas)
soma_notas = sum(lista_notas_lidas)
media_notas = soma_notas / qtd_notas

lista_notas_maior_que_media = []
lista_notas_menor_que_7 = []

for i in lista_notas_lidas:
    if i > media_notas:
        lista_notas_maior_que_media.append(i)
    if i < 7:
         lista_notas_menor_que_7.append(i)

qtd_notas_maior_que_media = len(lista_notas_maior_que_media)
qtd_notas_menor_que_7 = len(lista_notas_menor_que_7)

print(f"Quantidade de valores lidos: {qtd_notas}")
print(f"Soma dos valores: {soma_notas}")
print(f"Média dos valores: {round(media_notas, 2)}")
print(f"Quantidade de valores acima da media: {qtd_notas_maior_que_media}")
print(f"Quantidade de valores abaixo de 7: {qtd_notas_menor_que_7}")