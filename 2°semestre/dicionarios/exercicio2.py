'''
Escreva um programa em Python que crie uma lista de 7 dicionários, a qual deve conter os seguintes dados: 

Código do Produto; 
Nome (string); 
Categoria (string, ex: "Eletrônicos", "Escritório"); 
Quantidade em Estoque (inteiro); 
Fornecedor (string); 
Preço Unitário (float) 

Em seguida, exiba todos os produtos da loja. 
'''

lista_produto = []

for i in range(2):
    codigo = int(input("Digite o código do produto: "))
    nome = input("Digite o nome do produto: ")
    categoria = input("Digite a categoria do produto: ")
    quantidade_estoque = int(input("Digite a quantidade no estoque: "))
    fornecedor = input("Digite o nome do fornecedor: ")
    preco = float(input("Digite o preço unitário do produto: "))

    dados_produto = {
        'codigo': codigo,
        'nome': nome,
        'categoria': categoria,
        'quantidade_estoque': quantidade_estoque,
        'fornecedor': fornecedor,
        'preco': preco
    }

    lista_produto.append(dados_produto)

for i in range(len(lista_produto)):
    for chave, valor in lista_produto[i].items():
        print(f"{chave}:{valor}")
    print("---------------------------")