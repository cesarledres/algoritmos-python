'''
Escreva um programa em Python para ler 12 elementos inteiros para uma lista A. Construir uma lista B de mesmo tipo e
dimensão, observando a seguinte lei de formação: "Todo elemento da lista A que for ímpar deve ser multiplicado por 2;
caso contrário, o elemento da lista A deve permanecer constante". Apresentar a lista B.
'''
listaA = []
listaB = []


for i in range(12):
    num = int(input("Digite um número inteiro: "))
    listaA.append(num)

    if num % 2 != 0:
        listaB.append(num*2)
    else:
        listaB.append(num)

print(listaA)
print(listaB)