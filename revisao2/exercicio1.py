'''
Escreva um programa em Python para ler 10 valores e escrever quantos desses valores lidos
estão no intervalo [10,20] (incluindo os valores 10 e 20 no intervalo) e quantos deles
estão fora deste intervalo. Nesse caso, utilize a estrutura de repetição “for”.
'''
qtd_intervalo = 0
qtd_fora = 0

for i in range(5):
    num = int(input("Digite um número inteiro: "))

    if num >= 10 and num <= 20:
        qtd_intervalo += 1
    else:
        qtd_fora += 1

print(f"A quantidade de números entre o intervalo de 10 a 20 é {qtd_intervalo}")
print(f"A quantidade de números fora do intervalo é {qtd_fora}")