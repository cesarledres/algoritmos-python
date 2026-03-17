# Exemplo 4: Verificar e exibir se um numero esta dentro ou fora de um intervalo

'''
OPERADORES LOGICOS MAIS USADOS

* and (e): o resultado final eh verdadeiro se todas as condicoes
forem verdadeiras. Basta uma condicao ser falsa para o resultado ser falso.

* or (ou): o resultado final e falso se todas as condicoes forem falsas. Basta uma condicao ser verdadeira para o resultado ser verdade.

'''

# intervalo: entre 10 e 100, inclusive

numero = int(input("Digite um numero inteiro: "))

if (numero >= 10 and numero <= 100):
    print("O numero esta dentro do intervalo")
else:
    print("O numero esta fora do intervalo")



