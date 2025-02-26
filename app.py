import sqlite3

conexao = sqlite3.connect('banco.db')

cursor = conexao.cursor()
# cursor.execute('''CREATE TABLE cliente (id int primary key, nome_empresa text, cnpj text, observacao text, status boolean, contato varchar, endereco text );''')
# cursor.execute('''CREATE TABLE compromisso (id int primary key, id_cliente, data text, horario text, observacao text, status boolean, foreign key (id_cliente) references cliente(id) on delete cascade );''')
# cursor.execute('''CREATE TABLE contas_a_receber (id int primary key,valor_a_pagar text, data_lancamento text,data_vencimento text, observacao text, id_cliente, foreign key (id_cliente) references cliente(id) on delete cascade )''')


# cursor.execute(''' INSERT INTO cliente (nome, idade) VALUES ('Nome Falso', '25')''')
# cursor.execute('''DROP TABLE cliente''')
# conexao.commit()

# cursor.execute('''SELECT * from cliente''')

# rows = cursor.fetchall()
# for row in rows:
#     print(row)
