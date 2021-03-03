from flask import Flask, render_template, url_for, redirect,request, session
from ouath import *
from spotifyapiclient import *
import time


app = Flask(__name__)
app.secret_key = "sdUBIB2312jNBI"
app.config['SESSION_COOKIE_NAME'] = "Diversify"

OUATH_RESPONE = ''
ouath_client = SpotifyOuathClient()
api_client = SpotifyApiClient()

@app.route('/')
def index():

    auth_url = ouath_client.get_auth_url()
    return render_template("login.html", url=auth_url)


@app.route("/redirect/")
def redirectPage():
    
    session.clear()
    auth_code = request.args.get('code')
    session[OUATH_RESPONE] = ouath_client.get_token_info(auth_code)

    return redirect(url_for('profilePage', _external=True))


@app.route("/profile")
def profilePage():

    token = get_token()
    user_info = api_client.get_user_info(token)
    username = user_info["display_name"]
    followers = user_info["followers"]["total"]
    spotify_link = user_info["external_urls"]["spotify"]
    user_type = (user_info["product"]).capitalize()

    if len(user_info["images"]) == 0:
        profile_pic = None
    else:
        profile_pic = user_info["images"][0]["url"]
    

    return render_template("profile.html", username = username, followers = followers, link = spotify_link, pic = profile_pic, type = user_type)
    

@app.route("/music")
def myMusic():

    return "fml"

@app.route("/analytics")
def analytics():

    return "cool backend"

@app.route("/new")
def new():

    return "my music taste is dogwater, help me find new tracks"


def get_token(): 
    token_response = session.get(OUATH_RESPONE)
    current_time = int(time.time())
    token_expiry = (token_response['expires_in']) + current_time

    if (current_time > token_expiry):
        new_token = ouath_client.refresh_token(token_response['refresh_token'])   #logic for refreshing access token
        return new_token['access_token']

    else:
        return token_response['access_token']


if __name__ == "__main__":
    app.run()

