import requests as re
from lxml import html
from datetime import datetime as dt 

class Scraper:
	"""A web-scraper that looks up what show's are going on in 
		portland, me and stores it in a PostgreSQL database for fun."""

	def __init__(self,url):
		# declare url variable to scrape for info
		self.url = url
		# set up website info
		self.call = re.get(url)

	def get_dates_and_shows(self):
		# use lxml library to get dates from html class tags
		self.tree = html.fromstring(self.call.content)
		# create a list of dates using xpath
		self.month = self.tree.xpath('//span[@class="month"]/text()')
		self.day = self.tree.xpath('//span[@class="date"]/text()')
		self.year = str(dt.now().year)
		self.events = self.tree.xpath('//div[@class="event_title"]/text()')

		# create single list of date strings from tuples of two html tags
		self.dates = [s + self.year for s in list(map(''.join,(zip(self.month,self.day))))]
		# self.datetime_shows = [dt.strptime(date, '%b %d %Y').date() for date in self.dates]  
		
		self.apoha_shows = list(map(' '.join,(zip(self.dates, self.events))))
		
		#!!! add feature to roll year over between dec/jan
		
		return self.apoha_shows


	def get_eventbrite(self):
		# use lxml library to get dates from html class tags
		self.ftree = html.fromstring(self.call.content)
		# create a list of dates using xpath
		self.fdates = self.ftree.xpath('//article[@id="live_events"]//time[@class="list-card__date"]/text()')
		self.fevents = self.ftree.xpath('//article[@id="live_events"]//div[@class="list-card__title"]/text()')
		
		# Ugly as sin, but only way I could figure out how to clean up eventbrite data.
		self.shows = list(map(''.join,(zip(self.fdates, self.fevents))))
		self.fshows = [i.replace('\n','').strip().split() for i in self.shows]
		self.eventbrite_shows = list(map(' '.join, self.fshows)) 
		
		return self.eventbrite_shows

	def get_songkick(self):
		# use lxml library to get dates from html class tags
		self.stree = html.fromstring(self.call.content)
		# create a list of dates using xpath
		self.sdates = self.stree.xpath('//li[@class="with-date"]/strong/time/text()')
		self.sevents = self.stree.xpath('//p[@class="artists summary"]/a/span/strong/text()')
		self.songkick_shows = list(map(' '.join,(zip(self.sdates, self.sevents))))
		
		return self.songkick_shows
	
	def report(self):
		self.aphoadion = self.get_dates_and_shows()
		self.eventbrite = self.get_eventbrite()
		self.songkick = self.get_songkick() 
		
		if self.aphoadion:
			print(">>>>>>>>>>>>>>APOHADION<<<<<<<<<<<<<<< \n", self.aphoadion)
		elif self.eventbrite:
			print(">>>>>>>>>>>>>>GENO'S<<<<<<<<<<<<<<<< \n", self.eventbrite)
		elif self.songkick:
			print(">>>>>>>>>>>>>>>>SUN TIKI<<<<<<<<<<<<<< \n", self.songkick)




# apoha = Scraper('https://www.theapohadiontheater.com/')
# sun_tiki = Scraper('https://www.songkick.com/venues/3951109-sun-tiki-studios')
# genos = Scraper('https://www.eventbrite.com/o/genos-rock-club-15681751194')

 
# apoha.report()
# genos.report()
# sun_tiki.report()