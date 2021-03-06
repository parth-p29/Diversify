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

    def get_user_top(self, access_token, limit, time_range, top_type):

        url = self.API_BASE_URL + f"/top/{top_type}?time_range={time_range}&limit={limit}"

        body = {
            "Authorization": f"Bearer {access_token}"
        }

        get = requests.get(url, headers=body)
        data = json.loads(get.text)
        data_dict = {}

        if top_type == "tracks":

            for i in range(limit):

                data_dict[data['items'][i]["name"]] = data['items'][i]["album"]["images"][1]["url"]
                                                                       
        else:

            for i in range(limit):

                data_dict[data['items'][i]["name"]] = data['items'][i]["images"][1]["url"]
       
                
        return data_dict


    def get_user_top_track_info(self, access_token, limit, time_range):

        url = self.API_BASE_URL + f"/top/tracks?time_range={time_range}&limit={limit}"

        body = {
            "Authorization": f"Bearer {access_token}"
        }

        get = requests.get(url, headers=body)
        data = json.loads(get.text)
        data_list = [[]]
    
        for i in range(limit):

            data_list[i].append(data['items'][i]["album"]['artists'][0]['name'])
            data_list[i].append(data['items'][i]["album"]['name'])

            if i+1 == limit:
                break
            else:
                data_list.append([])


        artist_name = (np.array(data_list))[:,0]
        album_name = (np.array(data_list))[:,1]


        return [artist_name, album_name]

        #turn into a 2d arry, cuz dicts deleted duplicates when you do .keys() or .values()