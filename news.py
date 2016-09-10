from py_bing_search import PyBingNewsSearch
from bs4 import BeautifulSoup
import urllib

def get_news_articles(query, limit=5):
	api_key = 'uMbXJDSBqOpPB696+Ez0s+NcznWvurhuAKUruZuWXTA'
	bing_news = PyBingNewsSearch(api_key, query)
	results = bing_news.search(limit=limit, format='json')
	return results

def get_text(list_of_news_articles):
	dict_of_text = {}
	for news_articles in list_of_news_articles:
		url = news_articles.url
		r = urllib.urlopen(url).read()
		soup = BeautifulSoup(r)
		# kill all script and style elements
		for script in soup(["script", "style"]):
		    script.extract()    # rip it out

		# get text
		text = soup.get_text()

		# break into lines and remove leading and trailing space on each
		lines = (line.strip() for line in text.splitlines())
		# break multi-headlines into a line each
		chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
		# drop blank lines
		text = '\n'.join(chunk for chunk in chunks if chunk)

		dict_of_text[url] = text

	return dict_of_text

def get_data(query):
	return get_text(get_news_articles('apple'))