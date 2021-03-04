import requests,json

class SpotifyApiClient():

    def __init__(self):

        self.API_BASE_URL = "https://api.spotify.com/v1/me"

    def get_user_info(self, access_token):

        body = {

            "Authorization" : f"Bearer {access_token}"
        }

        get = requests.get(self.API_BASE_URL, headers=body)

        data = json.loads(get.text)

        return data

    def get_user_top_tracks(self, access_token, limit, time_range):

        url = self.API_BASE_URL + f"/top/tracks?time_range={time_range}&limit={limit}"


        body = {

            "Authorization": f"Bearer {access_token}"

        }

        get = requests.get(url, headers=body)

        data = json.loads(get.text)

        #song_name_list = []
        #song_cover_image_list = []

        song_info = [[]]
        song_dict = {}

        for song_index in range(limit):

            song_info[song_index].append(data['items'][song_index]["name"])
            song_info[song_index].append(data['items'][song_index]["album"]["images"][1]["url"])
            song_info.append([])

            
        for i in range(limit):
            song_dict[data['items'][i]["name"]] = data['items'][i]["album"]["images"][1]["url"]
            

        return song_dict


"""
for song_index in range(limit):
    song_list.append(data["items"][song_index]["name"])

"""  



