from flask import Flask, request, render_template,jsonify
import os
from nyt import get_article_data
from spotify import get_artist_data, get_song_data
from genius import get_lyric
import re

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# Got to Q1
@app.route('/')
def home():
	return render_template("Q1.html")

# Go to index	
@app.route("/get-song", methods=['POST'])
def getSong():
    Artist_Names = []
    trackId = request.form.getlist('song-id')[0]
    name = request.form.getlist('artist-name')[0]
    NYTData = get_article_data(name)
    SongData = get_song_data(trackId)
    Number_Artists = 0
    while True:
        try:
            Artist_Names.append(SongData['artists'][Number_Artists]['name'])
            Number_Artists += 1 
        except:
            break
    song_name = re.sub("[\(\[].*?[\)\]]", "", SongData['name'])
    GeniusData = get_lyric("{song_name} {artist}".format(song_name = song_name, artist = name))
    lenght = len(Artist_Names)

    return render_template(
        "index.html",
        Song_Name_Display = SongData['name'],
        Image_Display = SongData['album']['images'][0]['url'],
        Song_Play = SongData['preview_url'],
        Headlines = NYTData["Headlines"],
        Snippets = NYTData["Snippets"],
        DisplayURL = GeniusData['URL'],
        DisplayLyric = GeniusData["lyrics"],
        Artist_Names = Artist_Names,
        lenght = lenght
    )

# Go to Q2
@app.route('/GetArtist', methods = ['POST'])  
def main():
    Artist_List = ['Drake', 'The Weekend', 'J Balvin']
    if request.method == 'POST':
        Picked_Artist_online= request.form.getlist('artist')
    Artists = [str(Artists) for Artists in Picked_Artist_online]
    a_Artists = "".join(Artists)
    Picked_Artist = int(a_Artists)
    Name = Artist_List[Picked_Artist]
    SpotifyData = get_artist_data(Picked_Artist)

    # Collect All the data to send to index.html
    return render_template(
        "Q2.html",
        Artist_Name_Display = Name,
        Tracks = map(lambda track: {'id': track['id'], 'name': track['name']}, SpotifyData)
        )
        
#Send Data to index.html
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug = True,
)