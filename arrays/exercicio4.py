'''
Desenvolva um programa que receba 10 números inteiros e os armazene em uma lista. Em seguida, o programa
deve encontrar o maior elemento e exibir sua posição (índice) na lista.
'''
lista = []

for i in range(10):
    num = int(input("Digite um número inteiro: "))
    lista.append(num)

maior_num = max(lista)
indice_maior_num = lista.index(maior_num)

print(f"O maior número da lista é {maior_num} e sua posição/índice na lista é {indice_maior_num} (começando apartir do 0)")