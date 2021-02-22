import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

lz_uri = 'spotify:artist:43ZHCT0cAZBISjO8DG9PnE' #jcole

spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="88bb7350722b4d3898b677e75a9a3d75",
                                                           client_secret="e8882c8fd78f4f5182130fe4c6f5110e"))



tracks = spotify.artist_top_tracks(lz_uri)   #returns a json with "tracks" as the key
#the value of tracks in an array of tracks
#in each element of the array... is the album where the track is, the name, the etc.....


for i in range (0,10):

    print(tracks['tracks'][i]['name'])
