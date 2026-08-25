import json

with open("alunos_idade.json","r",encoding="utf-8") as ArqAlunos:
    dados_arq = ArqAlunos.read()
    listaAlunos = json.loads(dados_arq)
    print(listaAlunos)
    print(f"Quinto aluno:{listaAlunos[4]}")
    print(f"Idade do quinto aluno: {listaAlunos[4]['idade']}")
    ArqAlunos.close()

with open("log.json", "r", encoding="utf-8") as ArqLog:
    dados_arq = ArqLog.read()
    listaLogs = json.loads(dados_arq)
    print(f"Tabela do primeiro evento: {listaLogs[0]['tableName']}")
    print(f"Primeira chave do fields do primeiro evento: {listaLogs[0]['fields']["1"]}")
    ArqLog.close()