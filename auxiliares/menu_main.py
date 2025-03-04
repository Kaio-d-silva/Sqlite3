from services.clientes_services import *
from auxiliares.auxiliares import marcacao_linha

def menu_opcoes():
    # tabelas = ["Clientes", "Agenda Compromisso","Contas a Receber" ]
    
    tabelas = {
        1 : "Clientes",
        2 : "Agenda Compromisso",
        3 : "Contas a Receber"
    }
    
    
    print("Oque deseja acessar ?")
    for tabela in tabelas:
        numero = tabela
        nome_tabela = tabelas[tabela]
        print(f"{numero} {nome_tabela}")
        

            
    tabela_selecionada = int(input("Numero escolido : "))
    marcacao_linha()
    analisa_escolha(tabelas,tabela_selecionada)
    
    status = ""
    return status

def analisa_escolha(tabelas,escolha):
    if escolha in tabelas:
        match escolha:
            case 1: # Clientes
                opcoes_cliente()
            case _:
                print("não foi")
    else:
        print("caiu no else")
def opcoes_cliente():
    funcoes_cliente = {
        1 :"cadastrar_cliente",
        2 :"alterar_cadastro",
        3 :"listar_clientes",
        4 :"inativar_cliente"    
    }
    
    print("Oque deseja fazer : ")
    for funcao in funcoes_cliente:
        numero = funcao
        nome_funcao = funcoes_cliente[funcao].replace("_"," ")
        print(f"{numero} {nome_funcao}")
    
    funcao_escolhida = int(input("Escolha o numero da função : "))
    marcacao_linha()
    match funcao_escolhida:
        case 1: # Cadastro cliente
            cadastrar_cliente()
        case 2: #Alterar cadastro
            alterar_cadastro()
        case 3: #Listar clientes
            listar_clientes()
        case 4: #Inativar cliente
            inativar_cliente()
        
            
    