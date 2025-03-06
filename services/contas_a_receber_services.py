import db

def lancar_conta_a_receber():
    cliente_id = int(input("Informe o Id do cliente : "))
    valor_a_pagar = float(input("Valor a pagar : "))
    data_lancamento = "hoje" # pegar lib time para pegar data de hoje
    print("Informe o vencimento")
    dia_vencimento = str(input("Dia do vencimento : ")) 
    mes_vencimento = str(input("Mes do vencimento : ")) 
    ano_vencimento = str(input("Ano do vencimento : ")) 
    data_vencimento = f"{dia_vencimento}/{mes_vencimento}/{ano_vencimento}"
    observacao = str(input("Observação : "))
    resposta = db.insere_conta_a_receber(cliente_id,valor_a_pagar,data_lancamento,data_vencimento,observacao)
    return resposta

def alterar_lancamento(id, coluna=None, alteracao=None):
    '''Você pode passar somente o ID do cliente e vizualizar uma tela com as opções de coluna, ou pode passar a coluna e alteração como argumento'''
    nome_tabela = 'contas_a_receber'
    
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
    resposta = db.altera_dados(nome_tabela,nome_coluna, alteracao, id)
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
    
def listar_lancamentos(*nome_coluna):
    '''Escolha as colunas que deseja filtrar ou use " * " para ter todos os dados. Não use " * " e colunas no mesmo argumento'''
    
    valor_de_busca = ",".join(nome_coluna)
    resposta = db.listar_dados(valor_de_busca, "contas_a_receber")
    return resposta

    
def inativar_lancamento(id):
    coluna = "status"
    alteracao = False
    resposta = alterar_lancamento(id, coluna=coluna, alteracao=alteracao)
    return resposta