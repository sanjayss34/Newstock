import news
from textblob import TextBlob
import parser
import datetime


def get_probabilities(map_of_articles, max_delta):
	polarities = {}
	for article in map_of_articles.keys():
		text = map_of_articles[article][0]
		date_unicode = map_of_articles[article][1]
		date_datetime = parser.parse(date_unicode)
		delta = map_of_articles[article][2]
		weighted_score = ((max_delta - delta) * (blob.sentiment.polarity))/max_delta

		blob = TextBlob(text)
        polarities[article] = (date_unicode, weighted_score)
	return polarities

def get_data(query):
	news_tuple = news.get_data(query)
	return get_probabilities(news_tuple[0], news_tuple[1])

'''
def get_probabilities(map_of_articles):
    polarities = {}
    for article in map_of_articles.keys():
        text = map_of_articles[article][0]
        date = map_of_articles[article][1]
        blob = TextBlob(text)
        print(blob.sentiment.polarity)
        polarities[article] = (str(date), blob.sentiment.polarity**(1-blob.sentiment.subjectivity))
    return polarities

def get_data(query, dates):
    article_data = news.get_data(query, dates)
    print(len(article_data.keys()))
    return get_probabilities(article_data)
'''
