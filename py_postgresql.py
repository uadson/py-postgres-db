import psycopg2
from config import config


def connect():
	""" Conectando a um servidor Postgresql"""

	conn = None

	try:
		# lendo os parâmetros da conexão

		params = config()

		print('Conectando ao banco de dados PostgreSQL...')

		conn = psycopg2.connect(**params)

		# criando um cursor

		cur = conn.cursor()

		# executando

		print('Versão do banco de dados PostgreSQL')

		cur.execute('SELECT version()')


		# mostrando a versão do servidor

		db_version = cur.fetchone()

		print(db_version)

		# encerrando a comunicação com o PostgreSQL

		cur.close()

	except (Exception, psycopg2.DatabaseError) as error:
		print(error)

	finally:

		if conn is not None:
			conn.close()
			print('Conexão do Banco de Dados Encerrada.')


if __name__ == '__main__':
	connect()