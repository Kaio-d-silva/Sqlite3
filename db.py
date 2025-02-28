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


def altera_dados_cliente():
    try:
        cursor.execute(f'''UPDATE CLIENTES SET ''')
        return "Dados do cliente alterados"
    except:
        return "Dados do clientes não alterados"
    
    
