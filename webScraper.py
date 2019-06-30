import requests as re
from lxml import html

class Scraper:
	"""A web-scraper that looks up what show's are going on in 
		portland, me and reports them back to user (method of report TBD)."""

	def __init__(self,url):
		# set variables to scrape pages for info
		self.url = url
		# set up website info
		self.call = re.get(url)
		# self.text = self.call.text /// test to make sure call worked (debug)

		# use lxml library to get dates from html class tags
		self.tree = html.fromstring(self.call.content)
		# create a list of dates using xpath
		self.month = self.tree.xpath('//span[@class="month"]/text()')
		self.day = self.tree.xpath('//span[@class="date"]/text()') 
		#create single list of date tuples from two html tags
		self.dates = list(map(''.join,(zip(self.month,self.day))))
			


apoha = Scraper('https://www.theapohadiontheater.com/')

print(apoha.dates)