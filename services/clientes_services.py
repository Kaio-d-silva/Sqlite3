import db

def cadastrar_cliente():
    nome_empresa = input("Digite o nome_empresa: ") 
    cnpj = input("Digite o cnpj: ")
    observacao = input("Digite a observacao: ")
    contato = input("Digite o contato: ")
    endereco = input("Digite o endereco: ")
    resposta = db.insere_cliente(nome_empresa, cnpj,observacao,contato, endereco)
    return resposta

