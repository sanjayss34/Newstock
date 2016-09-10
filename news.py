from py_bing_search import PyBingNewsSearch

def get_news_articles(query, limit=30):
	api_key = 'uMbXJDSBqOpPB696+Ez0s+NcznWvurhuAKUruZuWXTA'
	bing_news = PyBingNewsSearch(api_key, query)
	results = bing_news.search(limit=limit, format='json')
	return results

