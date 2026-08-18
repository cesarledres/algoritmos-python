'''
Uma função com um parâmetro n que verifique e mostre se ele é par ou ímpar;
'''

def mostra_se_par_ou_impar(n):
    if n % 2 == 0:
        return "par"
    return "impar"

num = int(input("Digite um numero para verfificar se é par ou impar: "))

print(f"O numero é {mostra_se_par_ou_impar(num)}")