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
    session['time_frame'] = "short_term"


    return redirect(url_for('profilePage', _external=True))


@app.route("/profile")
def profilePage():

    a_token = get_token()

    request_data = api_client.get_user_info(a_token)
    user_info = request_data[0]
    username = user_info["display_name"]
    followers = user_info["followers"]["total"]
    spotify_link = user_info["external_urls"]["spotify"]
    
    if len(user_info["images"]) == 0:
        profile_pic = None
    else:
        profile_pic = user_info["images"][0]["url"]


    playlist_info = request_data[1]
    num_of_playlists = len(playlist_info['items']) 

    user_follow_info = request_data[2]
    num_of_followed_artists = len(user_follow_info['artists']['items'])

    return render_template("profile.html", username = username, followers = followers, link = spotify_link, pic = profile_pic, playlists = num_of_playlists, follows=num_of_followed_artists)
    

@app.route("/music")
def myMusic():

    return configure_user_top('music.html')


@app.route('/change-time/<string:id>')
def changeTime(id):

    session['time_frame'] = id

    return redirect(url_for('myMusic', _external=True))


@app.route('/info/<string:id>')
def info(id):

    return id

@app.route('/more')

def more():

    return configure_user_top('more.html')


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

def configure_user_top(html_page):

    a_token = get_token()
    time_frame = session.get('time_frame')

    try:
        user_top_tracks = api_client.get_user_top_info(a_token, 10, time_frame, "tracks")
        user_top_artists = api_client.get_user_top_info(a_token, 10, time_frame, "artists")

    except IndexError:
        return "Sorry your account has no music data :("

    songs = user_top_tracks[0]
    song_ids = user_top_tracks[1]
    song_covers = user_top_tracks[2]
    song_artists = user_top_tracks[3]
    song_albums = user_top_tracks[4]

    artists = user_top_artists[0]
    artist_ids = user_top_artists[1]
    artist_covers = user_top_artists[2]

    return render_template(html_page, songs = songs, song_ids = song_ids, song_covers = song_covers, song_artists = song_artists, song_albums = song_albums, artists = artists, artist_ids = artist_ids, artist_covers = artist_covers, zip=zip, time = time_frame)

if __name__ == "__main__":
    app.run()

