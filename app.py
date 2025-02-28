# from services.clientes_services import cadastrar_cliente,altarar_cadastro


# status = cadastrar_cliente()
# altarar_cadastro()


# import sqlite3

# conn = sqlite3.connect('banco.db')

# cursor = conn.cursor()


# cursor.execute('''SELECT sql FROM sqlite_master WHERE type='clientes';''')

# rows = cursor.fetchall()
# for row in rows:
#     print("teste")
#     print(row)

# import sqlite3

# # Conectando ao banco de dados SQLite
# conexao = sqlite3.connect('banco.db')

# # Criando um cursor para executar comandos
# cursor = conexao.cursor()

# # Nome da tabela da qual você deseja listar as colunas
# nome_tabela = 'cliente'

# # Executando o comando PRAGMA para obter informações sobre a tabela
# cursor.execute(f"PRAGMA table_info({nome_tabela});")

# # Obtendo os resultados
# colunas = cursor.fetchall()

# # Imprimindo o nome das colunas
# for coluna in colunas:
#     print(coluna[1])  # A segunda posição contém o nome da coluna

# # Fechando a conexão
# conexao.close()

from services.clientes_services import *

status = altarar_cadastro(1)
print(status)
# cadastrar_cliente()