import requests as re

class Scraper:
	"""A web-scraper that looks up what show's are going on in 
		portland, me and reports them back to user (method of report TBD)."""

	def __init__(self,url):
		# set variables to scrape pages for info
		self.url = url
		
		self.call = re.get(url)
		self.text = text(call)		


apoha = Scraper('https://www.theapohadiontheater.com/')
print(apoha.text)
