import requests
import os
import random
from dotenv import load_dotenv, find_dotenv


AUTH_URL = 'https://accounts.spotify.com/api/token'
#BASE_URL = 'https://api.spotify.com/v1/browse/new-releases'

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

random_number = random.randint(0,2)

#Artist in order: Drake, The Weekend, J Balvin
Artist_List = ['3TVXtAsR1Inumwj472S9r4', '1Xyo4u8uXC1ZmMpatF05PJ', '1vyhD5VmyZ7KMfW5gqLgo5']
Display_Artist = Artist_List[random_number]
BASE_URL = 'https://api.spotify.com/v1/artists/%s/top-tracks' %(Display_Artist)
r = requests.get(BASE_URL, 
                headers=headers,
                params={'market': 'US'} )
                

d = r.json()
Song_Name = d['tracks'][0]['album']['name']
Artist_Name = d['tracks'][0]['album']['artists'][0]['name']
Image = d['tracks'][0]['album']['images'][0]['url']
Preview = d['tracks'][0]['preview_url']
print(Song_Name)
print(Artist_Name)
print(Image)
print(Preview)




    