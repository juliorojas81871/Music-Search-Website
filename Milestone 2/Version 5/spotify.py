from flask import Flask, request, render_template,jsonify
import os
import requests
from dotenv import load_dotenv, find_dotenv
import random

load_dotenv(find_dotenv())

def getAuthHeaders ():
    # Aurtization URL for Spotify 

    AUTH_URL = 'https://accounts.spotify.com/api/token'
    # get data from .env
    
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
    
    return headers
    

Artist_List_ID = ['3TVXtAsR1Inumwj472S9r4', '1Xyo4u8uXC1ZmMpatF05PJ', '1vyhD5VmyZ7KMfW5gqLgo5']
Artist_List = ['Drake', 'The Weekend', 'J Balvin']

def get_song_data(song):
    headers = getAuthHeaders()
    Spotify_BASE_URL = 'https://api.spotify.com/v1/tracks/%s' %(song)
    SpotifyResponse = requests.get(Spotify_BASE_URL, headers=headers, params={'market': 'US'})
    SpotifyData = SpotifyResponse.json()
    return SpotifyData
    
def get_artist_data (Picked_Artist):
    headers = getAuthHeaders()
    #Artist in order: Drake, The Weekend, J Balvin
    Display_Artist = Artist_List_ID[Picked_Artist]
    Name = Artist_List[Picked_Artist]
    
    # Sending request to retirve data from Spotify
    # Will get back .json at the end
    Spotify_BASE_URL = 'https://api.spotify.com/v1/artists/%s/top-tracks' %(Display_Artist)
    SpotifyResponce = requests.get(Spotify_BASE_URL, 
                    headers=headers,
                    params={'market': 'US'} )
    SpotifyData = SpotifyResponce.json()

    return SpotifyData['tracks']
    