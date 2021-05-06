import psycopg2
from config import config


def create_tables():

	"""Criando tabelas em banco de dados PostgreSQL"""

	commands = (

		"""
		CREATE TABLE vendedores (
			vendedores_id SERIAL PRIMARY KEY,
			vendedor_nome VARCHAR(255) NOT NULL
		)
		""",

		"""
		CREATE TABLE papeis (
			papel_id SERIAL PRIMARY KEY,
			papel_nome VARCHAR(255) NOT NULL
		)	
		""",

		"""
		CREATE TABLE papel_desenho (
			papel_id INTEGER PRIMARY KEY,
			extensao_arquivo VARCHAR(5) NOT NULL,
			dados_desenho BYTEA NOT NULL,
			FOREIGN KEY (papel_id)
			REFERENCES papeis (papel_id)
			ON UPDATE CASCADE ON DELETE CASCADE
		)
		""",

		"""
		CREATE TABLE vendedor_papeis (
			vendedores_id INTEGER NOT NULL, 
			papel_id INTEGER NOT NULL,
			PRIMARY KEY (vendedores_id, papel_id),
			FOREIGN KEY (vendedores_id)
			REFERENCES vendedores (vendedores_id)
			ON UPDATE CASCADE ON DELETE CASCADE,

			FOREIGN KEY (papel_id)
			REFERENCES papeis (papel_id)
			ON UPDATE CASCADE ON DELETE CASCADE
		)
		""")


	conn = None

	try:

		params = config()

		conn = psycopg2.connect(**params)

		cur = conn.cursor()

		for command in commands:
			cur.execute(command)

		cur.close()

		conn.commit()

	except (Exception, psycopg2.DatabaseError) as error:
		print(error)

	finally:

		if conn is not None:
			conn.close()


if __name__ == '__main__':
	create_tables()