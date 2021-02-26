from flask import Flask, render_template, url_for, redirect
from spotify import *
from secrets import *

app = Flask(__name__)

#sp = spotipy.oauth2.SpotifyOAuth(client_id, client_secret, redirect_uri, scope="playlist-modify-private user-top-read", cache_path=".cache")
#access_token = sp.get_cached_token()['access_token']
user = SpotifyCient()

authurl = user.sp_ouath.get_authorize_url()
print(authurl)
#user = spotipy.Spotify(access_token)
#auth_url = sp.get_authorize_url()


@app.route('/')
def index():

    return render_template('index.html')


'''
if __name__ == "__main__":
    app.run(debug=True)
'''
#{"access_token": "BQDjTNtLuIwJNA6F33bgv7TX7RLJprC4GG8Ganbzc92GRtfarR6hRIDi2OIb3n0An1QyJQv8s6sh2Fl4wAv8IUuHaApoUqNmgjTDnfPhdp-DKf2YQwjwMO7iUjGToZoO3RtIWfWAJboPA_Y9Ke-lwJR2Gycu1S47DSevBnyjnMVmxaykXJjUhy67", "token_type": "Bearer", "expires_in": 3600, "refresh_token": "AQDuyF415GTx4qH-soq1s4Yt7ZSf-o5vq3Th-4J6N8treukVnjutUt4y85Y1nZqVdUlvgDfohk7yUyF337op24YsSJcugguiTJ_3IvVYDvlWbNHpJTeuymbSm17HTGHAiQs", "scope": "user-library-read user-top-read", "expires_at": 1614324258}