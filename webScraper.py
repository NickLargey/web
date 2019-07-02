import requests as re
from lxml import html
from datetime import datetime

class Scraper:
	"""A web-scraper that looks up what show's are going on in 
		portland, me and reports them back to user (method of report TBD)."""

	def __init__(self,url):
		# set variables to scrape pages for info
		self.url = url
		# set up website info
		self.call = re.get(url)
		# self.text = self.call.text /// test to make sure call worked (debug)

	def get_dates_and_shows(self):
		# use lxml library to get dates from html class tags
		self.tree = html.fromstring(self.call.content)
		# create a list of dates using xpath
		self.month = self.tree.xpath('//span[@class="month"]/text()')
		self.day = self.tree.xpath('//span[@class="date"]/text()')
		self.events = self.tree.xpath('//div[@class="event_title"]/text()')
		self.year = str(datetime.now().year) 
		# create single list of date strings from tuples of two html tags
		self.dates = [s + self.year for s in list(map(''.join,(zip(self.month,self.day))))]
		self.shows = list(map(' '.join,(zip(self.dates, self.events))))
		#!!! add feature to roll year over between dec/jan
		print(self.shows)

	def get_eventbrite(self):
		# use lxml library to get dates from html class tags
		self.ftree = html.fromstring(self.call.content)
		# create a list of dates using xpath
		self.fdates = self.ftree.xpath('//article[@id="live_events"]//time[@class="list-card__date"]/text()')
		self.fevents = self.ftree.xpath('//article[@id="live_events"]//div[@class="list-card__title"]/text()')
		
		# Ugly as sin, but only way I could figure out how to clean up eventbrite data.
		self.shows = list(map(''.join,(zip(self.fdates, self.fevents))))
		self.fshows = [i.replace('\n','').strip().split() for i in self.shows]
		self.ffshows = list(map(' '.join, self.fshows)) 
		
		print(self.ffshows)

	def get_songkick(self):
		# use lxml library to get dates from html class tags
		self.stree = html.fromstring(self.call.content)
		# create a list of dates using xpath
		self.sdates = self.stree.xpath('//li[@class="with-date"]/strong/time/text()')
		self.sevents = self.stree.xpath('//p[@class="artists summary"]/a/span/strong/text()')
		self.shows = list(map(' '.join,(zip(self.sdates, self.sevents))))
		
		print(self.shows)

apoha = Scraper('https://www.theapohadiontheater.com/')
sun_tiki = Scraper('https://www.songkick.com/venues/3951109-sun-tiki-studios')
genos = Scraper('https://www.eventbrite.com/o/genos-rock-club-15681751194')

print(apoha.get_dates_and_shows())
print(genos.get_eventbrite())
print(sun_tiki.get_songkick())