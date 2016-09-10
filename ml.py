import news
from textblob import TextBlob

def get_probabilities(map_of_articles):
	polarities = {}
	for article in map_of_articles.keys():
		text = map_of_articles[article][0]
		date = map_of_articles[article][1]
		blob = TextBlob(text)
		polarities[article] = (date, blob.sentiment.polarity)
	return polarities

def get_data(query):
	return get_probabilities(news.get_data(query))