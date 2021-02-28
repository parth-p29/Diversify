from secrets import *
import requests
import json

class SpotifyOuath():

    def __init__(self):

        self.CLIENT_ID = "58023d39e03146ae8b95a3443638037c"
        self.CLIENT_SECRET = "d5ab5a0d102b4c8c934a81acdc542e24"
        self.REDIRECT_URI = "http://localhost:5000/redirect/"
        self.SCOPE = "user-top-read"
        self.OAUTH_AUTHORIZE_URL = "https://accounts.spotify.com/authorize"
        self.OAUTH_TOKEN_URL = "https://accounts.spotify.com/api/token"
    
    def get_auth_url(self):

        payload = {

            "client_id": self.CLIENT_ID,
            "response_type": "code",
            "redirect_uri": self.REDIRECT_URI,
            "scope": self.SCOPE
        }

        auth_url = requests.get(self.OAUTH_AUTHORIZE_URL, params=payload).url
        
        return auth_url
