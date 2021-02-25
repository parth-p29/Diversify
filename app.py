import spotipy
from spotipy.oauth2 import SpotifyOAuth
from secrets import *

class SpotifyCient:

    def __init__ (self):
 
        self.spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id, client_secret, redirect_uri, scope="playlist-modify-private user-top-read"))
        #self.spotify = spotipy.oauth2.SpotifyAuthBase(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope="playlist-modify-private user-top-read")
    
    
    
    def create_new_playlist(self, user_id, name):

        self.spotify.user_playlist_create(user_id, name, public=False, collaborative=False, description="new playlist")


    def get_top_tracks(self, limit, time_range):

        results = self.spotify.current_user_top_tracks(limit=limit, time_range=time_range)

        for track_idx in range(limit):

            print(results['items'][track_idx]['name'])



    def get_top_artists(self, limit, time_range):

        results = self.spotify.current_user_top_artists(limit=limit, time_range=time_range)

        for track_idx in range(limit):

            print(results['items'][track_idx]['name'])

    

user = SpotifyCient()

auth = spotipy.oauth2.SpotifyAuthBase
user.get_top_tracks(10, "long_term")
user.get_top_artists(5, "short_term")
#user.create_new_playlist("9ii7f67pvtetvztlv2nv779li", "cool playlist")

