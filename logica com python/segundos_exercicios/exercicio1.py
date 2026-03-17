'''
O custo de um carro novo ao consumidor é a soma do custo de fábrica com a porcentagem do distribuidor
e dos impostos (aplicados ao custo de fábrica). Supondo que o percentual do distribuidor seja de 28% e
os impostos de 45%, escrever um algoritmo para solicitar o custo de fábrica de um carro, calcular e
escrever o custo final ao consumidor.
'''

custo_fabrica = float(input("Informe o custo de fabrica: "))

percentual_distribuidor = float(round(custo_fabrica * 0.28))
print(f"O percentual do distribuidor é R$ {percentual_distribuidor}")

percentual_impostos = float(round(custo_fabrica * 0.45))
print(f"O percentual de imposto é R$ {percentual_impostos}")

custo_final = float(round(custo_fabrica + percentual_distribuidor + percentual_impostos))

print(f"Somando tudo, o custo final para o consumidor é R$ {custo_final}")
