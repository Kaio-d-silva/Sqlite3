import sqlite3

conn = sqlite3.connect('banco.db')

cursor = conn.cursor()

def insere_cliente(nome_empresa, cnpj,observacao,contato, endereco, status=True):
    try:
        cursor.execute(f'''INSERT INTO cliente (nome_empresa ,cnpj ,observacao ,contato ,endereco, status ) VALUES ("{nome_empresa}" ,"{cnpj}" ,"{observacao}" ,"{contato}" ,"{endereco}", "{status}");''')
        conn.commit()
        return "Cliente inserido com sucesso"
    except:
        return "Não deu certo"


def altera_dados_cliente(tabela, coluna, alteracao, id):
    try:
        # print(f"UPDATE CLIENTES SET {coluna[1]} = '{alteracao}' WHERE id = {id}")
        cursor.execute(f'''UPDATE {tabela} SET {coluna[1]} = '{alteracao}' WHERE id = {id}''')
        conn.commit()
        return "Dados do cliente alterados"
    except:
        return "Dados do clientes não alterados"
    
    
