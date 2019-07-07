import psycopg2
from webScraper import Scraper
from config import config

"""Add scraped data to portland_shows table in postgres"""

apoha = Scraper('https://www.theapohadiontheater.com/').get_dates_and_shows()
sun_tiki = Scraper('https://www.songkick.com/venues/3951109-sun-tiki-studios').get_songkick()
genos = Scraper('https://www.eventbrite.com/o/genos-rock-club-15681751194').get_eventbrite()

scraped = Scraper('https://www.theapohadiontheater.com/')

params = config()
# connect to the PostgreSQL server
conn = psycopg2.connect(**params)
cur = conn.cursor()

# apohadion = .get_dates_and_shows()
# genos = 

sql = "INSERT INTO portland_shows (apohadion, genos, sun_tiki) VALUES (%s, %s, %s);"
for obj in zip(apoha, genos, sun_tiki):
    cur.execute(cur.mogrify(sql, obj))
conn.commit()

cur.close()
conn.close()