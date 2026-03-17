'''
Um condomínio possui 20 blocos e para uma correta administração possui dois síndicos: o sr José que
administra os blocos de 1 a 10 e o sr Hamilton que administra os blocos de 11 a 20. Escreva um algoritmo
que pergunte ao usuário em qual bloco ele mora e escreva na tela qual o síndico responsável.
'''

bloco_usuario = int(input("Informe o bloco em que você mora: "))

if bloco_usuario >= 1 and bloco_usuario <= 20:
    if bloco_usuario <= 10:
        print("O síndico responsável é o Sr. José.")
    else:
        print("O síndico responsável é o Sr. Hamilton.")
else:
    print("Esse bloco não pertence ao condomínio.")