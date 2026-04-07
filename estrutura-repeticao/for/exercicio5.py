'''
Ler um valor N e imprimir todos os valores inteiros entre 1 (inclusive) e N (inclusive). Considere que o N será sempre maior que ZERO.
'''

n = int(input("Digite um número para exibir do 1 até este: "))

if n > 0:
    for cont in range(1, n+1):
        print(cont)
else:
    print("O valor de N deve ser sempre maior que 0.")