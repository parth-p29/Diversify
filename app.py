import spotipy
from spotipy.oauth2 import SpotifyOAuth
from secrets import client_id, client_secret, redirect_uri
'''
client_id="88bb7350722b4d3898b677e75a9a3d75"
client_secret="e8882c8fd78f4f5182130fe4c6f5110e"
redirect_uri="http://localhost:8888/callback/"
'''
class SpotifyCient:

    def __init__ (self):

        self.CLIENT_ID = client_id
        self.CLIENT_SECRET = client_secret
        self.REDIRECT_URI = redirect_uri

    def get_top_tracks(self, limit, time_range, scope):

        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(self.CLIENT_ID, self.CLIENT_SECRET, self.REDIRECT_URI, scope))

        results = sp.current_user_top_tracks(limit=limit, time_range=time_range)

        for track_idx in range(limit):

            print(results['items'][track_idx]['name'])


        

user = SpotifyCient()

user.get_top_tracks(10, "long_term", "user-top-read")



        

'''
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="88bb7350722b4d3898b677e75a9a3d75",
                                               client_secret="e8882c8fd78f4f5182130fe4c6f5110e",
                                               redirect_uri="http://localhost:8888/callback/",
                                               scope="user-top-read"))  #the scope determines how much access you have of the user's info
                                               #different request endpoints require different scopes


sp2 = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="88bb7350722b4d3898b677e75a9a3d75",
                                               client_secret="e8882c8fd78f4f5182130fe4c6f5110e",
                                               redirect_uri="http://localhost:8888/callback/",
                                               scope="user-library-read"))


results = sp.current_user_top_artists(limit=2, offset=0, time_range="long_term")

for track_idx in range(2):

    print(results['items'][track_idx]['name'])



results = sp.current_user_top_tracks(limit=20, offset=0, time_range="medium_term")
print(results)
'''


'''
lz_uri = 'spotify:artist:1Xyo4u8uXC1ZmMpatF05PJ' #abel

CLIENT_ID = "88bb7350722b4d3898b677e75a9a3d75"
CLIENT_SECRET = "e8882c8fd78f4f5182130fe4c6f5110e"
SCOPE = ""
REDIRECT_URI = "http://localhost:8888/callback"#test

spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(CLIENT_ID, CLIENT_SECRET))



tracks = spotify.artist_top_tracks(lz_uri)   #returns a json with "tracks" as the key
#the value of tracks in an array of tracks
#in each element of the array... is the album where the track is, the name, the etc.....
 
for i in range (0,25):

    print(tracks['tracks'][i]['name'])
'''