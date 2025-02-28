import sqlite3

conexao = sqlite3.connect('banco.db')

cursor = conexao.cursor()
cursor.execute('''CREATE TABLE cliente (id INTEGER PRIMARY KEY AUTOINCREMENT, nome_empresa text, cnpj text, observacao text, status boolean, contato varchar, endereco text );''')
cursor.execute('''CREATE TABLE compromisso (id INTEGER PRIMARY KEY AUTOINCREMENT, id_cliente, data text, horario text, observacao text, status boolean, foreign key (id_cliente) references cliente(id) on delete cascade );''')
cursor.execute('''CREATE TABLE contas_a_receber (id INTEGER PRIMARY KEY AUTOINCREMENT,valor_a_pagar text, data_lancamento text,data_vencimento text, observacao text, id_cliente, foreign key (id_cliente) references cliente(id) on delete cascade )''')


conexao.commit()

# cursor.execute('''SELECT * from cliente''')

# rows = cursor.fetchall()
# for row in rows:
#     print(row)