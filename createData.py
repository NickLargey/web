import psycopg2
import datetime
from datetime import date
from webScraper import Scraper
from config import config

"""Add scraped data to portland_shows table in postgres"""

apoha = Scraper('https://www.theapohadiontheater.com/').get_dates_and_shows()
sun_tiki = Scraper('https://www.songkick.com/venues/3951109-sun-tiki-studios').get_songkick()
genos = Scraper('https://www.eventbrite.com/o/genos-rock-club-15681751194').get_eventbrite()

base = date.today()
date_list = [base + datetime.timedelta(days=x) for x in range(0, 100)]
fdate_list = [x.strftime("%b %d %Y") for x in date_list] 

print(fdate_list)
params = config()
# connect to the PostgreSQL server
conn = psycopg2.connect(**params)
cur = conn.cursor()

sql_time = "INSERT INTO portland_shows(date_of_show) VALUES (%s)"
for obj in zip(fdate_list):
	cur.execute(cur.mogrify(sql_time, obj))
	
sql = "INSERT INTO portland_shows (apohadion, genos, sun_tiki) VALUES (%s, %s, %s);"
for obj in zip(apoha, genos, sun_tiki):
    cur.execute(cur.mogrify(sql, obj))
conn.commit()

cur.close()
conn.close()