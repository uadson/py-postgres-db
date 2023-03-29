import psycopg2
from time import sleep
from config import db

def connect():

	conn = None

	try:
		print("Connecting to the database PostgreSQL ...")
		sleep(1.5)

		conn = psycopg2.connect(**db)
		cursor = conn.cursor()

		print("Database Version")
		sleep(1.5)
		
		cursor.execute('SELECT version()')
		db_version = cursor.fetchone()
		print(db_version)

		cursor.close()
	
	except(Exception, psycopg2.DatabaseError) as error:
		print(error)

	finally:
		if conn is not None:
			conn.close()
			print('Finished connection with database')
			sleep(1.5)


if __name__ == '__main__':
	connect()
