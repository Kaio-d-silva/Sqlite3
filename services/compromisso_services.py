import db
from auxiliares.auxiliares import marcacao_linha

def cadastrar_compromisso():
    cliente_fk = input('Informe o ID do cliente: ')
    data = input("Informe a data do compromisso: ") 
    horario = input("Informe o horário do compromisso: ")
    observacao = input("Alguma observação sobre o seu compromisso?: ")
    status = True
    resposta = db.insere_dados_compromisso(cliente_fk, data, horario, observacao, status)
    return resposta

def alterar_compromisso(coluna=None, alteracao=None):
    id_compromisso = input("Informe o ID do registro que deseja alterar: ")
    nome_tabela = 'compromisso'
    db.cursor.execute(f'PRAGMA table_info ({nome_tabela});')
    colunas_tabela = db.cursor.fetchall()

    if coluna == None:
        marcacao_linha()
        exibir_mensagem(colunas_tabela)

        alterar_dado = int(input('Informe o dado a ser alterado: '))
        alteracao = input('Informe o novo valor: ')
        marcacao_linha()

        dados_tabela = colunas_tabela[alterar_dado - 1]
        nome_coluna = dados_tabela[1]
    else:
        nome_coluna = coluna

    resposta = db.altera_dados(nome_tabela, nome_coluna, alteracao, id_compromisso)
    return resposta

#  Mensagem referente a alteração do cadastro
def exibir_mensagem(colunas):
    # Retira a coluna ID, ela nao pode ser alterada
    colunas.pop(0)

    index = 1
    for valor in colunas:
        print(f"{index} {valor[1]}")
        index += 1
    print("")

def inativar_compromisso():
    coluna = "status"
    alteracao = False
    resposta = alterar_compromisso(coluna=coluna, alteracao=alteracao)
    return resposta

def listar_compromissos():
    resposta = db.listar_dados("compromisso")
    marcacao_linha()
    return resposta