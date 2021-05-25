import os
import requests
from dotenv import load_dotenv, find_dotenv
from bs4 import BeautifulSoup

load_dotenv(find_dotenv())


def get_lyric(Picked_Song):
    try:
        # Genius API Section________________________________________________________________________________
        user_inputs = Picked_Song
        Genius_BASE_URL = 'https://api.genius.com'
        client_access_token = os.getenv('GENIUS_ACCESS_TOKEN')
    
        path = 'search/'
        request_uri = '/'.join([Genius_BASE_URL, path])
        params = {'q': user_inputs}
        token = 'Bearer {}'.format(client_access_token)
        headers = {'Authorization': token}
        
        GeniusResponce = requests.get(request_uri, params=params, headers=headers)
        GeniusData = GeniusResponce.json()
        URL = GeniusData['response']['hits'][0]['result']['url']
    
        #to get the lyrics out of the page I used beautifulsoup in the following way.
        page = requests.get(URL)
        html = BeautifulSoup(page.text, 'html.parser')
        lyrics = html.find('div', class_='lyrics').get_text()
        
        return {
            'URL': URL,
            'lyrics': lyrics,
        }
    except:
        return {
            'URL': None,
            'lyrics': "Failed to get lyrics"
        }
