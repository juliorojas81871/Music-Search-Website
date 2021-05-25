import os
import requests
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv()) # This is to load your API keys from .env

BASE_URL = 'https://api.nytimes.com/svc/search/v2/articlesearch.json'

def get_article_data(Name):
    """ Returns a list of headlines about a given topic """

    params = {
        'q': Name,
        'api-key': os.getenv('NYT_KEY'),
    }

    response = requests.get(BASE_URL, params=params)
    NYTData = response.json()
    print(NYTData)
    articles = NYTData['response']['docs']

    def get_headline(article):
        return article['headline']['main']

    def get_snippet(article):
        return article['snippet']

    Headlines = map(get_headline, articles)
    Snippets = map(get_snippet, articles)

    return {
        'Headlines': list(Headlines),
        'Snippets': list(Snippets),
    }
