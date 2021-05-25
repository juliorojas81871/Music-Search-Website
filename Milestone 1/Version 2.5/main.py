from flask import Flask, render_template
import requests
import os
from dotenv import load_dotenv, find_dotenv
import random

Spotify_AUTH_URL = 'https://accounts.spotify.com/api/token'

load_dotenv(find_dotenv())

auth_response = requests.post(Spotify_AUTH_URL, {
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
Artist_List_ID = ['3TVXtAsR1Inumwj472S9r4', '1Xyo4u8uXC1ZmMpatF05PJ', '1vyhD5VmyZ7KMfW5gqLgo5']
Artist_List = ['Drake', 'The Weekend', 'J Balvin']
print('0 = Drake, 1 =The Weekend, 2 = J Balvin')
Picked_Artist = int(input('Please Pick one of the Following Artists: '))
Display_Artist = Artist_List_ID[Picked_Artist]
Name = Artist_List[Picked_Artist]

Spotify_BASE_URL = 'https://api.spotify.com/v1/artists/%s/top-tracks' %(Display_Artist)
r = requests.get(Spotify_BASE_URL, 
                headers=headers,
                params={'market': 'US'} )
                
NYT_BASE_URL = 'https://api.nytimes.com/svc/search/v2/articlesearch.json'
r2 = requests.get(NYT_BASE_URL, 
                params={'q': Name,
                        'api-key': os.getenv('NYT_KEY') } )
                

d = r.json()
d2 = r2.json()
Song_Names = []
Artist_Names = []
Articles = []

for i in range (0,3):
    Song_Names.append(d['tracks'][i]['album']['name'])
print(' ')    
for p in range(len(Song_Names)):
    print('%s: %s' % (p, Song_Names[p]))
Picked_Song = int(input('Please pick one of the Previous Stated Songs: '))
print (Song_Names[Picked_Song])
Number_Artists = 0

while True:
    try:
        Artist_Names.append(d['tracks'][0]['album']['artists'][Number_Artists]['name'])
        Number_Artists += 1 
    except:
        break

Image = d['tracks'][0]['album']['images'][0]['url']
Preview = d['tracks'][Picked_Song]['preview_url']
print(Image)
print(Preview)
for i in range(0,3):
    Articles.append(d2['response']['docs'][i]['headline']['main'])
for p in range(len(Articles)):
    print('%s' % (Articles[p])) 
    