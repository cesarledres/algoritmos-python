# Exemplo de exportação de uma lista de dicionários para um arquivo json

import json

lista_contatos = []

for i in range(2):
    nome = input("Digite o nome do contato: ")
    celular = input("Digite o celular do contato: ")
    dados_contato = {
        'Nome':nome,
        'Celular':celular
    }
    lista_contatos.append(dados_contato)

# Exportar os dados da lista para um arquivo json

with open ("dados_contato.json", "w", encoding="utf-8") as ArqContato:
    json.dump(lista_contatos, ArqContato, ensure_ascii=False)
    ArqContato.close()