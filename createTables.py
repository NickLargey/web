import psycopg2
from config import config
 
 
def create_table():
	""" create tables in the PostgreSQL database"""
	command = (
		"""
		CREATE TABLE IF NOT EXISTS portland_shows (
			date_of_show DATE PRIMARY KEY,
			Apohadion VARCHAR(5000),
			genos VARCHAR(5000),
			sun_tiki VARCHAR(5000))
			"""
		)
	conn = None
	try:
		# read the connection parameters
		params = config()
		# connect to the PostgreSQL server
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		# create table one by one
		# for command in commands:
		cur.execute(command)
		# close communication with the PostgreSQL database server
		cur.close()
		# commit the changes
		conn.commit()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			print("Table set")
			conn.close()
 
 
if __name__ == '__main__':
	create_table()