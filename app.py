from flask import Flask, render_template
import spotipy

from secrets import *

app = Flask(__name__)

sp = spotipy.oauth2.SpotifyOAuth(client_id, client_secret, redirect_uri, scope="playlist-modify-private user-top-read", cache_path=".cache")
access_token = sp.get_cached_token()['access_token']

user = spotipy.Spotify(access_token)
auth_url = sp.get_authorize_url()
print(f'<a href="{auth_url}">login</a>')

@app.route('/')
def index():

    return render_template("login.html")



if __name__ == "__main__":
    app.run(debug=True)

