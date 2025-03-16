import os
from db import listar_dados

def marcacao_linha():
    print(40 * "-")
    
def lista_opcoes(opcoes):
    for opcao in opcoes:
        enumerador = opcao
        # Caso tenha _ ele retira.
        nome_funcao = opcoes[enumerador].replace("_"," ")
        print(f"{enumerador} {nome_funcao}")
    print("")
    
def limpar_terminal():
    if os.name == "nt":
        os.system("cls")    
    else:
        os.system("clear")
        


# Função que tem a finalidade de fazer um filtro no select, nao esta em uso atualmente
def filtro_listar_dados(nome_tabela, *nome_coluna):
    '''Escolha as colunas que deseja filtrar ou use não passe nenhuma para ter todos os dados'''
    # Se nenhuma coluna for passada como argumento ele usa o valor * no select
    if not nome_coluna:
        nome_coluna = "*"
    
    valor_de_busca = ",".join(nome_coluna)
    resposta = listar_dados(valor_de_busca, nome_tabela)
    marcacao_linha()
    return resposta