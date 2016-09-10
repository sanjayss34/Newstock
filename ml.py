import news
from textblob import TextBlob
import parser

def get_probabilities(map_of_articles):
    polarities = {}
    for article in map_of_articles.keys():
        text = map_of_articles[article][0]
        date = map_of_articles[article][1]
        blob = TextBlob(text)
        print(blob.sentiment.polarity)
        polarities[article] = (str(date), blob.sentiment.polarity)
    return polarities

def get_data(query):
    article_data = news.get_data(query)
    print(len(article_data.keys()))
    return get_probabilities(article_data)
