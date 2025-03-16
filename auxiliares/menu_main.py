from services.clientes_services import *
from services.compromisso_services import *
from services.contas_a_receber_services import *
from auxiliares.auxiliares import marcacao_linha, lista_opcoes, limpar_terminal

def menu_opcoes():
    # tabelas = ["Clientes", "Agenda Compromisso","Contas a Receber" ]
    
    opcoes = {
        1 : "Clientes",
        2 : "Agenda Compromisso",
        3 : "Contas a Receber",
        4 : "Sair"
    }
    
    while True:
        limpar_terminal()
        print("****     Menu Opções     ****\n")
        lista_opcoes(opcoes)

        opcao_selecionada = input("Numero escolhido : ")
        marcacao_linha()
        
        resposta =  analisa_escolha(opcoes,opcao_selecionada)
        
        print(resposta)
        marcacao_linha()
        if resposta == "sair":
            break
    # return resposta

def analisa_escolha(tabelas,escolha):
    try:
        escolha_formatada = int(escolha)
        if escolha_formatada in tabelas:
            match escolha_formatada:
                case 1: # Clientes
                    resposta = opcoes_cliente()
                case 2: # Agenda Compromisso
                    resposta = opcoes_compromisso()
                case 3: # Contas a Receber
                    resposta = opcoes_contas_a_receber()
                case 4: # Sair
                    resposta = "sair"

            return resposta
    except:
        marcacao_linha()
        return "Escolha não permitida"
        
        
def opcoes_cliente():
    funcoes_cliente = {
        1 :"cadastrar_cliente",
        2 :"alterar_cadastro",
        3 :"listar_clientes",
        4 :"inativar_cliente",
        5 : "voltar"   
    }
    
    while True:
        limpar_terminal()
        print("****     Escolha uma Opção     ****\n")
        lista_opcoes(funcoes_cliente)
        
        try:
            funcao_escolhida = int(input("Escolha o numero da função : "))
            marcacao_linha()
        
            match funcao_escolhida:
                case 1: # Cadastro cliente
                    resposta = cadastrar_cliente()
                case 2: #Alterar cadastro
                    resposta = alterar_cadastro()
                case 3: #Listar clientes
                    # Colocar logica para ver quais colunas seram alteradas
                    resposta = listar_clientes()
                case 4: #Inativar cliente
                    resposta = inativar_cliente()
                case 5:
                    return "saindo opcoes cadastro"
            print(resposta)
            marcacao_linha()
        except:
            marcacao_linha()
            print("Opção invalida")
            marcacao_linha()
            
        input("De um enter para continuar ")
            
        
           

# Coloque suas funções aqui dentro, e siga o padrão do match case da função "opcoes clientes"
def opcoes_compromisso():
    funcoes_compromisso = {
        1:"Cadastrar compromisso",
        2:"Alterar compromisso",
        3:"Exibir compromissos",
        4:"Ocultar compromisso",
        5:"voltar"
    }

    
    while True:
        limpar_terminal()
        print("****     Escolha uma Opção     ****\n")
        lista_opcoes(funcoes_compromisso)

        try:
            funcao_escolhida = int(input("Escolha o numero da função : "))
            marcacao_linha()
        
            match funcao_escolhida:
                case 1:
                    resposta = cadastrar_compromisso()
                case 2:
                    resposta = alterar_compromisso()
                case 3:
                    resposta = listar_compromissos()
                case 4:
                    resposta = inativar_compromisso()    
                case 5:     
                    return "Saindo de opcoes compromisso"
            print(resposta) 
            marcacao_linha()
        except:
            marcacao_linha()
            print("Opção invalida")
            marcacao_linha()
        
        input("De um enter para continuar ")

            
def opcoes_contas_a_receber():
    funcoes_contas_a_receber = {
        1:"lancar conta a receber",
        2:"alterar lancamento",
        3:"exibir lancamentos",
        4:"inativar lancamento",
        5:"Voltar"
    }
    
    while True:
        limpar_terminal()
        print("****     Escolha uma Opção     ****\n")
        lista_opcoes(funcoes_contas_a_receber)
        
        try:            
            funcao_escolhida = int(input("Escolha o numero da função : "))
            marcacao_linha()
            
            match funcao_escolhida:
                case 1: # Lancar conta a receber
                    resposta = lancar_conta_a_receber()
                case 2: # alterar_lancamento
                    resposta = alterar_lancamento()
                case 3: # listar_lancamentos
                    resposta = listar_lancamentos()
                case 4: # Inativar lançamento
                    resposta = inativar_lancamento()
                case 5: # Voltar
                    return "Saindo opções conta a receber"                
            print(resposta)    
            marcacao_linha()
        except:
            print("Opção invalida")
        input("De um enter para continuar ")

    