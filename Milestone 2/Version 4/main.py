from flask import Flask, render_template
import requests
import os
from dotenv import load_dotenv, find_dotenv
from bs4 import BeautifulSoup
import re

app = Flask(__name__)

@app.route('/')
def Artist():
    # Spotify API section________________________________________________________________________________________
    # Aurtization URL for Spotify 
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
    # create header for request
    headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
    }
    
    #Artist in order: Drake, The Weekend, J Balvin
    Artist_List_ID = ['3TVXtAsR1Inumwj472S9r4', '1Xyo4u8uXC1ZmMpatF05PJ', '1vyhD5VmyZ7KMfW5gqLgo5']
    Artist_List = ['Drake', 'The Weekend', 'J Balvin']
    print('____________________________________________________________')
    print('\n 0 = Drake, 1 = The Weekend, 2 = J Balvin')
    Picked_Artist = int(input('Please Pick one of the Following Artists: '))
    Display_Artist = Artist_List_ID[Picked_Artist]
    Name = Artist_List[Picked_Artist]
    
    # Sending request to retirve data from Spotify
    # Will get back .json at the end
    Spotify_BASE_URL = 'https://api.spotify.com/v1/artists/%s/top-tracks' %(Display_Artist)
    SpotifyResponce = requests.get(Spotify_BASE_URL, 
                    headers=headers,
                    params={'market': 'US'} )
    
    # NYT API Section________________________________________________________________________________
    # Sending request to retirve data from New York Times
    # Will get back .json at the end                
    NYT_BASE_URL = 'https://api.nytimes.com/svc/search/v2/articlesearch.json'
    NYTResponce = requests.get(NYT_BASE_URL, 
                    params={'q': Name,
                            'api-key': os.getenv('NYT_KEY') } )
                            
    
    # Open the data collected 
    SpotifyData = SpotifyResponce.json()
    NYTData = NYTResponce.json()
    print (SpotifyData)
    
    
    Song_Names = []
    Artist_Names = []
    Articles = []
    
    for i in range (0,3):
        Song_Names.append(SpotifyData['tracks'][i]['name'])
            
    print(' ')    
    for p in range(len(Song_Names)):
        print('%s: %s' % (p, Song_Names[p]))
    Picked_Song = int(input('Please pick one of the Previous Stated Songs: '))
    print('____________________________________________________________')

    Song_Name=Song_Names[Picked_Song]
    
    # To get multiple artist from the song and save it to Artist_Names List
    Number_Artists = 0
    while True:
        try:
            Artist_Names.append(SpotifyData['tracks'][0]['album']['artists'][Number_Artists]['name'])
            Number_Artists += 1 
        except:
            break
        
    length = int(len(Artist_Names))
    Image = SpotifyData['tracks'][0]['album']['images'][0]['url']
    Preview = SpotifyData['tracks'][Picked_Song]['preview_url']
    
    # To get multiple NYT articles save it to Articles List
    for i in range(0,3):
        Articles.append(NYTData['response']['docs'][i]['headline']['main'])
        
    # Genius API Section________________________________________________________________________________
    client_access_token = os.getenv('GENIUS_ACCESS_TOKEN')
    Genius_BASE_URL = 'https://api.genius.com'
    
    # Combining / joining the past two questions into 1
    # combining = []
    # combining.append(Song_Name)
    # combining.append(Name)
    # user_inputs = " ".join(combining)
    user_inputs = Song_Name
    
    path = 'search/'
    request_uri = '/'.join([Genius_BASE_URL, path])
    print(request_uri + user_inputs)
    params = {'q': user_inputs}
    token = 'Bearer {}'.format(client_access_token)
    headers = {'Authorization': token}
    
    GeniusResponce = requests.get(request_uri, params=params, headers=headers)
    GeniusData = GeniusResponce.json()
    URL = GeniusData['response']['hits'][0]['result']['url']
    print(URL)
    
    #to get the lyrics out of the page I used beautifulsoup in the following way.
    page = requests.get(URL)
    html = BeautifulSoup(page.text, 'html.parser')
    lyrics = html.find('div', class_='lyrics').get_text()

    # Collect All the data to send to index.html
    return render_template(
        "index.html",
        Song_Name_Display = Song_Name,
        Artist_Name_Display = Artist_Names,
        Image_Display = Image,
        Song_Play = Preview,
        Artist_Articles = Articles,
        Artist_Length=length,
        DisplayURL = URL,
        DisplayLyric = lyrics

        )
        
#Send Data to index.html
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug = True,
)