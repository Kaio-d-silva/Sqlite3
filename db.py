import sqlite3

conn = sqlite3.connect('banco.db')

cursor = conn.cursor()

def insere_cliente(nome_empresa, cnpj,observacao,contato, endereco, status=True):
    cursor.execute(f'''INSERT INTO cliente (nome_empresa ,cnpj ,observacao ,contato ,endereco, status ) VALUES ("{nome_empresa}" ,"{cnpj}" ,"{observacao}" ,"{contato}" ,"{endereco}", "{status}");''')
    conn.commit()
    return "Cliente inserido com sucesso"

teste = insere_cliente(nome_empresa="kaio",cnpj="1000",observacao="teste",contato="98588917", endereco="rua do caralho" )
print(teste)