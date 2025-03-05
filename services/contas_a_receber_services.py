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
