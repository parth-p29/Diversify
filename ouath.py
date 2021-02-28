import requests
import json
import base64
from urllib.parse import quote

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
            "scope": self.SCOPE,
        }

        auth_url = requests.get(self.OAUTH_AUTHORIZE_URL, params=payload).url
        
        #url_args = "&".join(["{}={}".format(key, quote(val)) for key, val in payload.items()])
        #auth_url = "{}/?{}".format(self.OAUTH_AUTHORIZE_URL, url_args)

        return auth_url

    def get_auth_and_refresh_tokens(self, auth_code):

        body = {
            "grant_type": "authorization_code",
            "code": str(auth_code),
            "redirect_uri": self.REDIRECT_URI,
            "client_id": self.CLIENT_ID,
            "client_secret": self.CLIENT_SECRET    
        }

        post = requests.post(self.OAUTH_TOKEN_URL, data=body)
        response_data = post.text
        return (response_data)

'''
        encoded = base64.b64encode(f"{self.CLIENT_ID}:{self.CLIENT_SECRET}")
        print(encoded)
        headers = {"Content-Type" : HEADER, "Authorization" : "Basic {}".format(encoded)} 
                    "client_id": self.CLIENT_ID,
            "client_secret": self.CLIENT_SECRET
'''


