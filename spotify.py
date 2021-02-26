import spotipy
from spotipy.oauth2 import SpotifyOAuth
from secrets import *

class SpotifyCient:

    def __init__ (self):
 
        self.sp_ouath = SpotifyOAuth(client_id, client_secret, redirect_uri, scope="user-library-read user-top-read")
        self.spotify = spotipy.Spotify(auth_manager=self.sp_ouath)

    def auth_url(self):
        
        return self.sp_ouath.get_authorize_url()


    def get_top_tracks(self, limit, time_range):

        results = self.spotify.current_user_top_tracks(limit=limit, time_range=time_range)
        track_list = []

        for track_idx in range(limit):

            track_list.append((results['items'][track_idx]['name']))

        return track_list


    def get_top_artists(self, limit, time_range):

        results = self.spotify.current_user_top_artists(limit=limit, time_range=time_range)

        for track_idx in range(limit):

            print(results['items'][track_idx]['name'])



#
#user = SpotifyCient()

#user.get_top_tracks(10, "long_term")
#user.get_top_artists(5, "short_term")
#user.create_new_playlist("9ii7f67pvtetvztlv2nv779li", "cool playlist")


#sp = SpotifyOAuth(client_id, client_secret, redirect_uri, scope="playlist-modify-private user-top-read", cache_path=".cache")