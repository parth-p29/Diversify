import requests,json
import numpy as np

class SpotifyApiClient():

    def __init__(self):

        self.API_BASE_URL = "https://api.spotify.com/v1/me"

    def get_user_info(self, access_token):

        body = {

            "Authorization" : f"Bearer {access_token}"
        }

        playlist_url = self.API_BASE_URL + "/playlists"
        followed_artist_url = self.API_BASE_URL + "/following?type=artist"

        user_info_get = requests.get(self.API_BASE_URL, headers=body)
        playlist_get = requests.get(playlist_url, headers=body)
        followed_artists_get = requests.get(followed_artist_url, headers=body)

        user_info_data = json.loads(user_info_get.text)
        playlists_data = json.loads(playlist_get.text)
        followed_artists_data = json.loads(followed_artists_get.text)

        return [user_info_data, playlists_data, followed_artists_data]


    def get_user_top_info(self, access_token, limit, time_range, top_type):

        url = self.API_BASE_URL + f"/top/{top_type}?time_range={time_range}&limit={limit}"

        body = {
            "Authorization": f"Bearer {access_token}"
        }

        get = requests.get(url, headers=body)
        data = json.loads(get.text)
        data_collection_list = [ [] for _ in range(limit) ]
    
        for i in range(limit):
            data_collection_list[i].append(data['items'][i]["name"]) #top artist or track name [0]
            data_collection_list[i].append(data['items'][i]['id']) #top artist or track id [1]

            if top_type == "tracks":
                data_collection_list[i].append(data['items'][i]["album"]["images"][1]["url"]) # top track cover image [2]
                data_collection_list[i].append(data['items'][i]["album"]['artists'][0]['name']) #top track artist name [3]
                data_collection_list[i].append(data['items'][i]["album"]['name']) #top track album name [4]

            else:
                data_collection_list[i].append(data['items'][i]["images"][1]["url"]) #top artist cover image [2]

        if top_type == "tracks":
            output_list = []

            for col_idx in range (5):
                output_list.append((np.array(data_collection_list))[:,col_idx])

            return output_list

        else:
            output_list = []

            for col_idx in range (3):
                output_list.append((np.array(data_collection_list))[:,col_idx])

            return output_list


        #turn into a 2d arry, cuz dicts deleted duplicates when you do .keys() or .values()

    def get_track_or_artist_info(self, access_token, id):

        pass