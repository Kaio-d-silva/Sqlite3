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


def altera_dados(nome_tabela, nome_coluna, alteracao, id):
    try:
        cursor.execute(f'''UPDATE {nome_tabela} SET {nome_coluna} = '{alteracao}' WHERE id = {id}''')
        conn.commit()
        return f"Dados {nome_tabela} alterados"
    except Exception as e:
        return f"Dados do clientes não alterados : {e}"
    
    
def listar_dados(colunas_select, nome_tabela):
    try:
        cursor.execute(f'''SELECT {colunas_select} FROM {nome_tabela}''')
        linhas = cursor.fetchall()
        for linha in linhas:
            print(linha)
        
        return "Select deu certo"
    except Exception as e:
        return f"Não deu certo : {e}"
    
def insere_conta_a_receber(id_cliente,valor_a_pagar, data_lancamento, data_vencimento, observacao):
    try:
        cursor.execute(f'''INSERT INTO contas_a_receber (id_cliente,valor_a_pagar, data_lancamento, data_vencimento, observacao) VALUES ({id_cliente},{valor_a_pagar},"{data_lancamento}","{data_vencimento}","{observacao}")''')
        conn.commit()
        return f"Conta a receber inserida"
    except Exception as e:
        return f"Não deu certo : {e}"
    
def insere_dados_compromisso(cliente_fk, data, horario, observacao, status):
    try:
        cursor.execute(f'''INSERT INTO compromisso (id_cliente, data, horario, observacao, status ) VALUES ("{cliente_fk}", "{data}", "{horario}", "{observacao}", "{status}");''')
        conn.commit()
        return "Compromisso inserido com sucesso"
    except:
        return "Não deu certo"