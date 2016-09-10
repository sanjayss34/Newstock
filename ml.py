import news
from textblob import TextBlob

def get_probabilities(map_of_articles):
	polarities = {}
	for article in map_of_articles.keys():
		text = map_of_articles[article]
		blob = TextBlob(text)
		polarities[article] = blob.sentiment.polarity
	return polarities

print get_probabilities(news.get_data('apple'))