import psycopg2
from time import sleep
from config import db


class Postgres:

	def connect(self, db):

		conn = None

		try:
			print("Connecting to the database PostgreSQL ...")
			sleep(1.5)

			conn = psycopg2.connect(**db)
			return conn
		
		except(Exception, psycopg2.DatabaseError) as error:
			return error

	def create_table(self):
		"""
			Create a table on database
		"""
		sql_cmd = (
			"""
				CREATE TABLE cars (
					car_id SERIAL PRIMARY KEY,
					brand VARCHAR(50) NOT NULL,
					model VARCHAR(50) NOT NULL,
					price DECIMAL(10,2)
				)
			"""
		)
		conn = None
		try:
			conn = self.connect(db)
			cursor = conn.cursor()
			cursor.execute(sql_cmd)
			cursor.close()
			conn.commit()
		except (Exception, psycopg2.DatabaseError) as error:
			print(error)
		finally:
			if conn is not None:
				conn.close()
