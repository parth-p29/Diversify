import requests
import json



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

    def get_user_top_tracks(self, access_token):

        url = "https://api.spotify.com/v1/me/top/tracks"


        body = {

            "Authorization": f"Bearer {access_token}"

        }

        get = requests.get(url, headers=body)

        data = json.loads(get.text)

        return data



