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
    
    print("Qual dado voce quer alterar:")
    
    index = 1
    for valor in colunas:
        print(f"{index} {valor[1]}")
        index += 1
    print("")
        
    escolha = int(input(""))
    alteracao = input("Escreva o novo valor do dado : ")
    coluna = colunas[escolha-1]
    
    resposta = db.altera_dados_cliente(nome_tabela,coluna, alteracao, id)
    return resposta


def exibe_mensagem():
    pass