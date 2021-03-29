import requests, json
from dataclient import *

class SpotifyApiClient():

    def __init__(self, access_token):

        self.API_BASE_URL = "https://api.spotify.com/v1"
        self.auth_body = {
            "Authorization" : f"Bearer {access_token}"
        }

    def get_user_info(self):

        output_dict = lambda **data: data

        playlist_url = self.API_BASE_URL + "/me/playlists"
        followed_artist_url = self.API_BASE_URL + "/me/following?type=artist"

        user_info_get = requests.get(f"{self.API_BASE_URL}/me", headers=self.auth_body)
        playlist_get = requests.get(playlist_url, headers=self.auth_body)
        followed_artists_get = requests.get(followed_artist_url, headers=self.auth_body)

        user_info_data = json.loads(user_info_get.text)
        playlists_data = json.loads(playlist_get.text)
        followed_artists_data = json.loads(followed_artists_get.text)
        
        return output_dict(user_info=user_info_data, playlist_info=playlists_data, following_info=followed_artists_data)

    def get_user_top_info(self, limit, time_range, top_type):

        url = self.API_BASE_URL + f"/me/top/{top_type}?time_range={time_range}&limit={limit}"
        get = requests.get(url, headers=self.auth_body)
        data = json.loads(get.text)

        data_dict = {}

        for i in range(limit):

            data_dict[i] = {}
            data_dict[i]['name'] = data['items'][i]["name"]
            data_dict[i]['id'] = data['items'][i]["id"]

            if top_type == "tracks":
                data_dict[i]["image"] = data['items'][i]["album"]["images"][1]["url"]  #track cover image
                data_dict[i]["trackartistname"] = data['items'][i]["album"]['artists'][0]['name'] #artist who released track
                data_dict[i]["trackalbumname"] = data['items'][i]["album"]['name'] #album the track is in

            else:
                data_dict[i]['image'] = data['items'][i]["images"][1]["url"] #artist cover image

        return get_user_top_data(data_dict)

    def get_track_or_artist_info(self, type_id, info_type):

        output_dict = lambda **data: data

        url = self.API_BASE_URL + f"/{info_type}/{type_id}"
        get = requests.get(url, headers=self.auth_body)
        data = json.loads(get.text)

        popularity = data['popularity']
        name = data['name']

        if info_type == "artists":

            followers = data['followers']['total']
            genres = data['genres']
            image = data['images'][2]['url']

            return output_dict(followers=followers, genres=genres, name=name, image=image, popularity=popularity)
        
        else:
            artist_name = data['artists'][0]['name']

            return output_dict(name=name, artist=artist_name, popularity=popularity)

    def find_artists_from_songs(self, song_ids):

        url = self.API_BASE_URL + f"/tracks?ids={song_ids}"
        get = requests.get(url, headers=self.auth_body)
        data = json.loads(get.text)
        
        return [ artist['album']['artists'][0]['id'] for artist in data['tracks']] 

    def get_audio_features(self, track_id):

        output_dict = lambda **data: data

        url = self.API_BASE_URL + f'/audio-features/{track_id}'
        get = requests.get(url, headers=self.auth_body)
        data = json.loads(get.text)

        Danceability = data['danceability']
        Energy = data['energy']
        acousticness = data['acousticness']
        Speechiness = data['speechiness']
        Valence = data['valence']
        instrumentalness = data['instrumentalness']
        tempo = data['tempo']
        loudness = data['loudness']

        return output_dict(features=[Danceability, Energy, acousticness, Speechiness, Valence, instrumentalness], tempo=tempo, loudness=loudness)

    def get_audio_features_for_multiple_songs(self, ids):

        url = self.API_BASE_URL + f"/audio-features?ids={ids}"
        get = requests.get(url, headers=self.auth_body)
        data = json.loads(get.text)
        all_features = []

        for audio in data['audio_features']:

            features = [audio['danceability'], audio['energy'], audio['acousticness'],
                        audio['speechiness'], audio['valence'], audio['instrumentalness']]

            all_features.append(features)

        return all_features

    def get_multiple_track_or_artist_info(self, info_type, type_ids, feature):

        url = self.API_BASE_URL + f"/{info_type}?ids={type_ids}"
        get = requests.get(url, headers=self.auth_body)
        data = json.loads(get.text)
        all_pop = [pop[feature] for pop in data[info_type]]
        
        return all_pop

    def get_song_lyrics(self, song_artist, song_name):

        url = f"https://api.lyrics.ovh/v1/{song_artist}/{song_name}"
        
        try:
            get = requests.get(url, timeout=8)
        
        except:
            return "Lyrics not able to be analyzed"
        
        data = json.loads(get.text)
        lyrics = data['lyrics'].replace("\n","<br>")
     
        return lyrics

        
