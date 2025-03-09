import os

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
        
