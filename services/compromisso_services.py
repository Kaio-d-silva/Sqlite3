import db

def cadastrar_compromisso():
    data = input("Informe a data do compromisso: ") 
    horario = input("Informe o horário do compromisso: ")
    observacao = input("Alguma observação sobre o seu compromisso?: ")
    status = False
    resposta = db.insere_cliente(data, horario, observacao, status)
    return resposta

def alterar_compromisso():
    data = input("Informe a data do compromisso: ") 
    horario = input("Informe o horário do compromisso: ")
    observacao = input("Alguma observação sobre o seu compromisso?: ")
    status = False
    resposta = db.insere_cliente(data, horario, observacao, status)
    return resposta

def exibir_compromisso():
    data = input("Informe a data do compromisso: ") 
    horario = input("Informe o horário do compromisso: ")
    observacao = input("Alguma observação sobre o seu compromisso?: ")
    status = False
    resposta = db.insere_cliente(data, horario, observacao, status)
    return resposta

def ocultar_compromisso():
    data = input("Informe a data do compromisso: ") 
    horario = input("Informe o horário do compromisso: ")
    observacao = input("Alguma observação sobre o seu compromisso?: ")
    status = False
    resposta = db.insere_cliente(data, horario, observacao, status)
    return resposta
