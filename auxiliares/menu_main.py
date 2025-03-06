from services.clientes_services import *
from services.contas_a_receber_services import *
from auxiliares.auxiliares import marcacao_linha, lista_opcoes

def menu_opcoes():
    # tabelas = ["Clientes", "Agenda Compromisso","Contas a Receber" ]
    
    tabelas = {
        1 : "Clientes",
        2 : "Agenda Compromisso",
        3 : "Contas a Receber"
    }
    
    
    print("Oque deseja acessar ?")
    lista_opcoes(tabelas)
    
    tabela_selecionada = int(input("Numero escolido : "))
    marcacao_linha()
    resposta =  analisa_escolha(tabelas,tabela_selecionada)
    return resposta

def analisa_escolha(tabelas,escolha):
    if escolha in tabelas:
        match escolha:
            case 1: # Clientes
                resposta = opcoes_cliente()
            case 2: # Agenda Compromisso
                resposta = opcoes_agenda_compromisso()
            case 3: # Contas a Receber
                resposta = opcoes_contas_a_receber()
        
        return resposta
    else:
        return "Escolha não permitida"
        
        
def opcoes_cliente():
    funcoes_cliente = {
        1 :"cadastrar_cliente",
        2 :"alterar_cadastro",
        3 :"listar_clientes",
        4 :"inativar_cliente"    
    }
    
    print("Oque deseja fazer : ")
    lista_opcoes(funcoes_cliente)
    
    funcao_escolhida = int(input("Escolha o numero da função : "))
    marcacao_linha()
    match funcao_escolhida:
        case 1: # Cadastro cliente
            resposta = cadastrar_cliente()
        case 2: #Alterar cadastro
            cliente_id = int(input("Qual o ID do cliente : "))
            resposta = alterar_cadastro(cliente_id)
        case 3: #Listar clientes
            # Colocar logica para ver quais colunas seram alteradas
            resposta = listar_clientes("*")
        case 4: #Inativar cliente
            cliente_id = int(input("Qual o ID do cliente : "))
            resposta = inativar_cliente(cliente_id)
    return resposta        

# Coloque suas funções aqui dentro, e siga o padrão do match case da função "opcoes clientes"
def opcoes_agenda_compromisso():
    funcoes_agenda = {

    }            
    
def opcoes_contas_a_receber():
    funcoes_contas_a_receber = {
        1:"lancar_conta_a_receber",
        2:"alterar_lancamento",
        3:"exibir_lancamentos",
        4:"inativar_lancamento"
    }
    
    print("Oque deseja fazer : ")
    lista_opcoes(funcoes_contas_a_receber)
    
    funcao_escolhida = int(input("Escolha o numero da função : "))
    marcacao_linha()
    match funcao_escolhida:
        case 1: # Lancar conta a receber
            resposta = lancar_conta_a_receber()
        case 2: # alterar_lancamento
            lancamento_id = int(input("Qual o ID do lancamento : "))
            resposta = alterar_lancamento(lancamento_id)
        case 3: # listar_lancamentos
            resposta = listar_lancamentos("*")
        case 4: # Inativar lançamento
            lancamento_id = int(input("Qual o ID do lancamento : "))
            resposta = inativar_lancamento(lancamento_id)

            
    return resposta    
    
    