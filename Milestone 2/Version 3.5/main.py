from flask import Flask, render_template
import requests
import os
from dotenv import load_dotenv, find_dotenv
import random
from bs4 import BeautifulSoup
import re


app = Flask(__name__)

@app.route('/')
def Artist():
    # Spotify Authorization URL
    AUTH_URL = 'https://accounts.spotify.com/api/token'
    # get data from .env
    load_dotenv(find_dotenv())
    
    auth_response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': os.getenv('CLIENT_ID'),
        'client_secret': os.getenv('CLIENT_SECRET'),
    })
    
    # convert the response to JSON
    auth_response_data = auth_response.json()
    
    # save the access token
    access_token = auth_response_data['access_token']
    
    headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
    }
  
    #Artist in order: Drake, The Weekend, J Balvin
    Artist_List = ['3TVXtAsR1Inumwj472S9r4', '1Xyo4u8uXC1ZmMpatF05PJ', '1vyhD5VmyZ7KMfW5gqLgo5']
    # random generate a number between 0-2 in order to pick one of the artist in the list
    Artist_List2 = ['After Hours The Weeknd', 'The Weekend', 'J Balvin']

    random_number = random.randint(0,2)
    Display_Artist = Artist_List[random_number]
    
    # Sending request to retirve data from Spotify
    # Will get back .json at the end
    BASE_URL = 'https://api.spotify.com/v1/artists/%s/top-tracks' %(Display_Artist)
    r = requests.get(BASE_URL, 
                    headers=headers,
                    params={'market': 'US','include_groups': 'single', 'Default': 0} )

   
                        
    # Open the data collected 
    d = r.json()
    Song_Name = d['tracks'][0]['album']['name']
    Artist_Name = d['tracks'][0]['album']['artists'][0]['name']
    Image = d['tracks'][0]['album']['images'][0]['url']
    Preview = d['tracks'][0]['preview_url']

    client_access_token = os.getenv('GENIUS_ACCESS_TOKEN')
    base_url = 'https://api.genius.com'
    
    user_input = Artist_List2[0]
    
    path = 'search/'
    request_uri = '/'.join([base_url, path])
    print(request_uri + user_input)
    params = {'q': user_input}
    token = 'Bearer {}'.format(client_access_token)
    headers = {'Authorization': token}
    
    r2 = requests.get(request_uri, params=params, headers=headers)
    d2 = r2.json()
    URL = d2['response']['hits'][0]['result']['url']
    print(URL)
    
    #to get the lyrics out of the page I used beautifulsoup in the following way.
    page = requests.get(URL)
    html = BeautifulSoup(page.text, 'html.parser')
    lyrics = html.find('div', class_='lyrics').get_text()
    # print(lyrics)
    # Collect All the data to send to index.html
    return render_template(
        "index.html",
        Song_Name_Display = Song_Name,
        Artist_Name_Display = Artist_Name,
        Image_Display = Image,
        Song_Play = Preview, 
        DisplayLyric = lyrics
        )

#Send Data to index.html
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug = True,
)

    