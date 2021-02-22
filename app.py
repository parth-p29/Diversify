import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials


lz_uri = 'spotify:artist:1Xyo4u8uXC1ZmMpatF05PJ' #abel

CLIENT_ID = "88bb7350722b4d3898b677e75a9a3d75"
CLIENT_SECRET = "e8882c8fd78f4f5182130fe4c6f5110e"
SCOPE = ""
REDIRECT_URI = ""#test

spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(CLIENT_ID, CLIENT_SECRET))



tracks = spotify.artist_top_tracks(lz_uri)   #returns a json with "tracks" as the key
#the value of tracks in an array of tracks
#in each element of the array... is the album where the track is, the name, the etc.....

print(spotify.current_user())   
for i in range (0,25):

    print(tracks['tracks'][i]['name'])
