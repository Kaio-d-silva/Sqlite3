def marcacao_linha():
    print(50 * "-")
    
def lista_opcoes(opcoes):
    for opcao in opcoes:
        enumerador = opcao
        # Caso tenha _ ele retira.
        nome_funcao = opcoes[enumerador].replace("_"," ")
        print(f"{enumerador} {nome_funcao}")
    