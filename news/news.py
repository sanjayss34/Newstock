from py_bing_search import PyBingNewsSearch
query = 'Apple'
bing_news = PyBingNewsSearch(api_key, query)
result = bing_news.search(limit=10, format='json')