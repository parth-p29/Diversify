from flask import Flask, render_template, url_for, redirect,request, session
from ouath import *
from spotifyapiclient import *
import time


app = Flask(__name__)
app.secret_key="Diversify-App"


ouath_client = SpotifyOuathClient()
api_client = SpotifyApiClient()

@app.route('/')
def index():

    auth_url = ouath_client.get_auth_url()
    return render_template("login.html", url=auth_url)


@app.route("/redirect/")
def redirectPage():

    auth_code = request.args.get('code')
    auth_info = ouath_client.get_token_info(auth_code)

    session['ouath_info'] = auth_info
    session['start_time'] = int(time.time())


    return redirect(url_for('profilePage', _external=True))


@app.route("/profile")
def profilePage():

    a_token = get_token()

    user_info = api_client.get_user_info(a_token)
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

    a_token = get_token()
 
    user_top_tracks_short_term = api_client.get_user_top_tracks(a_token, 10, "short_term")
    user_top_tracks_medium_term = api_client.get_user_top_tracks(a_token, 10, "medium_term")
    user_top_tracks_long_term = api_client.get_user_top_tracks(a_token, 10, "long_term")

    short_term_songs = list(user_top_tracks_short_term.keys())
    short_term_song_covers = list(user_top_tracks_short_term.values())

    medium_term_songs = list(user_top_tracks_medium_term.keys())
    medium_term_song_covers = list(user_top_tracks_medium_term.values())

    long_term_songs = list(user_top_tracks_long_term.keys())
    long_term_song_covers = list(user_top_tracks_long_term.values())

    return render_template("music.html", st_songs=short_term_songs, st_cover=short_term_song_covers, zip=zip)

@app.route('/change-time')
def changeTime():

    return redirect(url_for('myMusic', _external=True))






@app.route("/analytics")
def analytics():

    return "cool backend"





@app.route("/new")
def new():

    return "my music taste is dogwater, help me find new tracks"


def get_token(): 
    
    ouath_info = session.get('ouath_info') #gets the user ouath info from the session
    start_time = session.get('start_time') #gets the start time from session
    current_time = int(time.time()) #sets the current time
    token_expiry = ouath_info['expires_in']  #sets the token expiry time which is 3600 seconds or 1 hour
    time_diff = current_time - start_time #subtracts current_time from the time when the access_token was first provided

    if (time_diff > token_expiry): #if the time difference passes 3600, a new access token is required

        new_token = ouath_client.refresh_token(ouath_info['refresh_token'])   #logic for refreshing access token
        start_time = int(time.time())
        return new_token['access_token']
    
    else:
        return ouath_info['access_token']





if __name__ == "__main__":
    app.run()

