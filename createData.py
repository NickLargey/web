import psycopg2
import datetime
from datetime import date
from webScraper import Scraper
from config import config
from psycopg2 import sql

"""Add scraped data to portland_shows table in postgres"""

apoha = Scraper('https://www.theapohadiontheater.com/').get_dates_and_shows()
sun_tiki = Scraper('https://www.songkick.com/venues/3951109-sun-tiki-studios').get_songkick()
genos = Scraper('https://www.eventbrite.com/o/genos-rock-club-15681751194').get_eventbrite()

base = date.today()
date_list = [base + datetime.timedelta(days=x) for x in range(0, 100)]
base_ = str(date.today())
params = config()
# connect to the PostgreSQL server
conn = psycopg2.connect(**params)
cur = conn.cursor()

# create the dates column as the primary key

sql_time = "INSERT INTO portland_shows(date_of_show) VALUES (%s) ON CONFLICT (date_of_show) DO NOTHING;"

# delete dates that have gone by
cur.execute(sql.SQL("DELETE FROM {} WHERE date_of_show<%s").format(sql.Identifier('portland_shows')), [base_])

for obj in zip(date_list):
	cur.execute(cur.mogrify(sql_time, obj))
	
# loop through returned dicts from Scraper and match key:value pairs in postgres
for k,v in apoha.items():
    cur.execute('''UPDATE portland_shows 
                         SET apohadion = (%s) 
                       WHERE date_of_show = (%s);''',(v,k))

for k,v in sun_tiki.items():
    cur.execute('''UPDATE portland_shows 
                         SET sun_tiki = (%s) 
                       WHERE date_of_show = (%s);''',(v,k))

for k,v in genos.items():
    cur.execute('''UPDATE portland_shows 
                         SET genos = (%s) 
                       WHERE date_of_show = (%s);''',(v,k))

conn.commit()

cur.close
conn.close()