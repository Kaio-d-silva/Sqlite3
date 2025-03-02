import db

def cadastrar_cliente():
    nome_empresa = input("Digite o nome_empresa: ") 
    cnpj = input("Digite o cnpj: ")
    observacao = input("Digite a observacao: ")
    contato = input("Digite o contato: ")
    endereco = input("Digite o endereco: ")
    resposta = db.insere_cliente(nome_empresa, cnpj,observacao,contato, endereco)
    return resposta

def alterar_cadastro(id, coluna=None, alteracao=None):
    '''Você pode passar somente o ID do cliente e vizualizar uma tela com as opções de coluna, ou pode passar a coluna e alteração como argumento'''
    nome_tabela = 'cliente'
    
    # Pega dados das tabelas
    db.cursor.execute(f"PRAGMA table_info({nome_tabela});")
    colunas = db.cursor.fetchall()
    
    if coluna == None:
        print(50*"-")
        exibir_mensagem(colunas)
        escolha = int(input("Qual dado voce quer alterar : "))
        alteracao = input("Escreva o novo valor do dado : ")
        print(50*"-")
    
        dados_coluna = colunas[escolha-1]
        nome_coluna = dados_coluna[1] 
    else:
        nome_coluna = coluna
    resposta = db.altera_dados_cliente(nome_tabela,nome_coluna, alteracao, id)
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
    
def listar_clientes(*nome_coluna):
    '''Escolha as colunas que deseja filtra ou use " * " para ter todos os dados. Não use " * " e colunas no mesmo argumento'''
    
    valor_de_busca = ",".join(nome_coluna)
    print(valor_de_busca)
    resposta = db.lista_clientes(valor_de_busca)
    return resposta
    
    
def inativar_cliente(id):
    coluna = "status"
    alteracao = False
    resposta = alterar_cadastro(id, coluna=coluna, alteracao=alteracao)
    return resposta

