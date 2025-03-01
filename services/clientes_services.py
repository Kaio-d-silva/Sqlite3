import db

def cadastrar_cliente():
    nome_empresa = input("Digite o nome_empresa: ") 
    cnpj = input("Digite o cnpj: ")
    observacao = input("Digite a observacao: ")
    contato = input("Digite o contato: ")
    endereco = input("Digite o endereco: ")
    resposta = db.insere_cliente(nome_empresa, cnpj,observacao,contato, endereco)
    return resposta

def altarar_cadastro(id):
    
    nome_tabela = 'cliente'
    
    db.cursor.execute(f"PRAGMA table_info({nome_tabela});")
    colunas = db.cursor.fetchall()
    
    print(50*"-")
    exibir_mensagem(colunas)
    escolha = int(input("Qual dado voce quer alterar : "))
    alteracao = input("Escreva o novo valor do dado : ")
    print(50*"-")
    
    coluna = colunas[escolha-1]
    
    resposta = db.altera_dados_cliente(nome_tabela,coluna, alteracao, id)
    return resposta


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
    
    
    