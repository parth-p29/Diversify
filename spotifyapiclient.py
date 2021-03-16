import requests,json



class SpotifyApiClient():

    def __init__(self, access_token):

        self.API_BASE_URL = "https://api.spotify.com/v1/me"
        self.URL2 = "https://api.spotify.com/v1"
        self.auth_body = {

            "Authorization" : f"Bearer {access_token}"
        }

    def get_user_info(self):

        playlist_url = self.API_BASE_URL + "/playlists"
        followed_artist_url = self.API_BASE_URL + "/following?type=artist"

        user_info_get = requests.get(self.API_BASE_URL, headers=self.auth_body)
        playlist_get = requests.get(playlist_url, headers=self.auth_body)
        followed_artists_get = requests.get(followed_artist_url, headers=self.auth_body)

        user_info_data = json.loads(user_info_get.text)
        playlists_data = json.loads(playlist_get.text)
        followed_artists_data = json.loads(followed_artists_get.text)

        return user_info_data, playlists_data, followed_artists_data


    def get_user_top_info(self, limit, time_range, top_type):

        url = self.API_BASE_URL + f"/top/{top_type}?time_range={time_range}&limit={limit}"

        get = requests.get(url, headers=self.auth_body)
        data = json.loads(get.text)

        name_list = []
        id_list = []
        track_cover_list = []
        track_artist_list = []
        track_album_list = []
        artist_cover_list = []

        for i in range(limit):
            name_list.append(data['items'][i]["name"])
            id_list.append(data['items'][i]["id"])

            if top_type == "tracks":
                track_cover_list.append(data['items'][i]["album"]["images"][1]["url"]) # top track cover image [2]
                track_artist_list.append(data['items'][i]["album"]['artists'][0]['name']) #top track artist name [3]
                track_album_list.append(data['items'][i]["album"]['name']) #top track album name [4]

            else:
                artist_cover_list.append(data['items'][i]["images"][1]["url"]) #top artist cover image [2]

        if top_type=="tracks":
            
            return name_list, id_list, track_cover_list, track_artist_list, track_album_list

        else:
            
            return name_list, id_list, artist_cover_list


    def get_track_or_artist_info(self, type_id, info_type):

        url = self.URL2 + f"/{info_type}/{type_id}"

        get = requests.get(url, headers=self.auth_body)
        data = json.loads(get.text)

        popularity = data['popularity']

        if info_type == "artists":

            followers = data['followers']['total']
            genres = data['genres']
            name = data['name']
            image = data['images'][2]['url']

            return followers, genres, name, image, popularity
        
        return popularity

    def get_audio_features (self, track_id):

        url = self.URL2 + f'/audio-features/{track_id}'
        
        get = requests.get(url, headers=self.auth_body)
        try:
            data = json.loads(get.text)

        except:
            print(get.status_code)

        Danceability = data['danceability']
        Energy = data['energy']
        acousticness = data['acousticness']
        Speechiness = data['speechiness']
        Valence = data['valence']
        instrumentalness = data['instrumentalness']
        tempo = data['tempo']
        loudness = data['loudness']

        return [Danceability, Energy, acousticness, Speechiness, Valence, instrumentalness], tempo, loudness

    def get_audio_features_for_multiple_songs(self, ids):

        url = self.URL2 + f"/audio-features?ids={ids}"

        get = requests.get(url, headers=self.auth_body)
        
        data = json.loads(get.text)

        print(get.status_code)

        all_features = []

        for audio in data['audio_features']:

            features = [audio['danceability'], audio['energy'], audio['acousticness'],
                        audio['speechiness'], audio['valence'], audio['instrumentalness']]

            all_features.append(features)

        return all_features

        