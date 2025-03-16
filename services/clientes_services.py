import db
from auxiliares.auxiliares import marcacao_linha
def cadastrar_cliente():
    nome_empresa = input("Digite o nome_empresa: ") 
    cnpj = input("Digite o cnpj: ")
    observacao = input("Digite a observacao: ")
    contato = input("Digite o contato: ")
    endereco = input("Digite o endereco: ")
    resposta = db.insere_cliente(nome_empresa, cnpj,observacao,contato, endereco)
    marcacao_linha()
    return resposta

def alterar_cadastro(coluna=None, alteracao=None):
    '''Você pode passar somente o ID do cliente e vizualizar uma tela com as opções de coluna, ou pode passar a coluna e alteração como argumento'''
    nome_tabela = 'cliente'
    cliente_id = int(input("Qual o ID do cliente : "))
    
    # Pega dados das tabelas
    db.cursor.execute(f"PRAGMA table_info({nome_tabela});")
    colunas = db.cursor.fetchall()
    
    if coluna == None:
        marcacao_linha()
        exibir_mensagem(colunas)
        escolha = int(input("Qual dado voce quer alterar : "))
        marcacao_linha()
        alteracao = input("Escreva o novo valor do dado : ")
        marcacao_linha()
    
        dados_coluna = colunas[escolha-1]
        nome_coluna = dados_coluna[1] 
    else:
        nome_coluna = coluna
    resposta = db.altera_dados(nome_tabela,nome_coluna, alteracao, cliente_id)
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
    
def listar_clientes():
    resposta = db.listar_dados("cliente")
    marcacao_linha()
    return resposta
    
    
def inativar_cliente():
    coluna = "status"
    alteracao = False
    resposta = alterar_cadastro(coluna=coluna, alteracao=alteracao)
    marcacao_linha()
    return resposta

