from py_bing_search import PyBingNewsSearch
from bs4 import BeautifulSoup
import urllib
import urllib2
import json

def get_company_name(symbol):
    symbol = symbol.upper()
    symbols_dict = {}
    for symbols_file_name in ['nasdaqlisted.txt', 'otherlisted.txt']:
        symbols_file = open(symbols_file_name, 'r+')
        symbols_lines = symbols_file.readlines()
        for i in range(1, len(symbols_lines)-1):
            info = symbols_lines[i].split('|')
            symbols_dict[info[0]] = info[1].split('-')[0]
        result = symbol
        if symbol in symbols_dict.keys():
            result = symbols_dict[symbol]
        print('result: ' + result)
    return result

def get_bing_news_articles(query, limit=100):
    api_key = 'uMbXJDSBqOpPB696+Ez0s+NcznWvurhuAKUruZuWXTA'
    bing_news = PyBingNewsSearch(api_key, query)
    results = bing_news.search(limit=limit, format='json')
    print(results)
    return results

def get_webhose_news_articles(query):
    print('before')
    api_token = "9efda9b1-2b8b-4382-b1f9-f190a89b269e"
    url_stub = "https://webhose.io"
    url = url_stub+"/search?token="+api_token+"&format=json&q=" + query+'&ts=1470938123396'
    count = 0
    posts = []
    while count < 2:
        data = urllib2.urlopen(url)
        json_data = json.loads(data.read())
        posts += json_data['posts']
        url = url_stub+json_data['next']
        count += 1
        print('done')
    return posts

def get_text(list_of_news_articles):
    dict_of_text = {}
    for news_articles in list_of_news_articles:
        # url = news_articles.url
        # date = news_articles.date
        url = str(news_articles['url'])
        date = str(news_articles['published'])

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

        dict_of_text[url] = (text, date)
    print(len(dict_of_text.keys()))
    return dict_of_text

def get_data(query):
	return get_text(get_webhose_news_articles(get_company_name(query)))
