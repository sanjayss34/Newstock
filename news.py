from py_bing_search import PyBingNewsSearch
from bs4 import BeautifulSoup
import urllib
import datetime
import parser

def get_news_articles(query, limit=5):
	api_key = 'uMbXJDSBqOpPB696+Ez0s+NcznWvurhuAKUruZuWXTA'
	bing_news = PyBingNewsSearch(api_key, query)
	results = bing_news.search(limit=limit, format='json')
	return results

def get_text(list_of_news_articles):
	dict_of_text = {}
	max_delta = 0;
	date_now = datetime.date.today()
	for news_articles in list_of_news_articles:
		url = news_articles.url
		date = news_articles.date

		date_datetime = parser.parse(date)
		date_delta = date_now - date_datetime
		delta = 0;
		if (date_delta.day):
			delta = delta + date_delta.day
		if (date_delta.month):
			delta = delta + 30 * date_delta.month
		if (date_delta.year):
			delta = delta + 365 * date_delta.year

		if (delta > max_delta):
			max_delta = delta

		r = urllib.urlopen(url).read()
		soup = BeautifulSoup(r)
		for script in soup(["script", "style"]):
		    script.extract()

		text = soup.get_text()

		lines = (line.strip() for line in text.splitlines())
		chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
		text = '\n'.join(chunk for chunk in chunks if chunk)

		dict_of_text[url] = (text, date, delta)
	return (dict_of_text, max_delta)

def get_data(query):
	return get_text(get_news_articles(query))