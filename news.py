from py_bing_search import PyBingNewsSearch
from bs4 import BeautifulSoup
import urllib

def get_news_articles(query, limit=30):
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
		dict_of_text[url] = soup.title.get_text() + '/n' + soup.body.get_text()
	return dict_of_text

