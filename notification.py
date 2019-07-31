"""Access postgres DB to get next few days of shows to text to myself"""
from createData import create_data
import psycopg2
from psycopg2 import sql
from twilio.rest import Client
from twilioInit import twilio_init
from config import config


create_data()

params = config()
# connect to the PostgreSQL server
conn = psycopg2.connect(**params)
cur = conn.cursor()

# load the table of shows
cur.execute(
	sql.SQL("SELECT * FROM {} ORDER BY {} ASC")
		.format(sql.Identifier('portland_shows'),sql.Identifier('date_of_show')))

# return the first 3 rows as a variable 
this_week = cur.fetchmany(3)

# init blank message to text
send ="" 

# format text
for row in this_week:
	date = str(row[0])
	a = str(row[1])
	g = str(row[2])
	st = str(row[3])
	send += '\n' + 'date: ' + date + '\n' + 'Apohadion: '+ a + '\n' + 'Genos: ' + g +'\n' + 'Sun Tiki: ' + st + '\n\n'


print(send)

conn.commit()
cur.close()
conn.close()

"""send a text for the next few days of shows"""
params = twilio_init()
client = Client(params[0], params[1])
message = client.messages.create(to=params[3], 
	from_=params[2], body=send)
