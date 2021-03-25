from flask import Flask, render_template, url_for, redirect, request, session
from oauth import *
from datanalysis import *
from spotifyapiclient import *
import time

app = Flask(__name__)
app.secret_key="Diversify-App"

oauth_client = SpotifyOauthClient()

@app.route('/')
def index():

    auth_url = oauth_client.get_auth_url()
    return render_template("login.html", url=auth_url)


@app.route("/redirect/")
def redirectPage():

    auth_code = request.args.get('code')
    auth_info = oauth_client.get_token_info(auth_code)

    session['oauth_info'] = auth_info
    session['start_time'] = int(time.time())
    session['time_frame'] = "short_term"

    return redirect(url_for('profilePage', _external=True))


@app.route("/profile")
def profilePage():

    api_client = init_api_client()
    request_data = api_client.get_user_info()

    user_info = request_data["user_info"]
    username = user_info["display_name"]
    followers = user_info["followers"]["total"]
    spotify_link = user_info["external_urls"]["spotify"]
    
    if len(user_info["images"]) == 0:
        profile_pic = None
    else:
        profile_pic = user_info["images"][0]["url"]

    playlist_info = request_data["playlist_info"]
    num_of_playlists = len(playlist_info['items']) 

    user_follow_info = request_data["following_info"]
    num_of_followed_artists = len(user_follow_info['artists']['items'])

    return render_template("profile.html", username = username, followers = followers, link = spotify_link, pic = profile_pic, playlists = num_of_playlists, follows=num_of_followed_artists)
    

@app.route("/music")
def myMusic():

    return configure_user_top('music.html', 10)

@app.route('/change-time/<string:id>')
def changeTime(id):
    
    if id[-1] == "M":
        session['time_frame'] = id[:-1]
        return redirect(url_for('more', _external=True))
    
    elif id[-1] == "A":
        session['time_frame'] = id[:-1]
        return redirect(url_for('analytics', _external=True))

    else:      
        session['time_frame'] = id
        return redirect(url_for('myMusic', _external=True))


@app.route('/info/<string:id>')
def info(id):

    api_client = init_api_client()

    if id[-1] == "T":
        track_id = id[:-1]

        try:
            track_popularity = (api_client.get_track_or_artist_info(track_id, "tracks"))['popularity']
            audio_info = api_client.get_audio_features(track_id)
            info_type="track"

            audio_features = audio_info['features']
            tempo = audio_info['tempo']
            loudness = audio_info['loudness']
            labels = ['Danceability', 'Energy', 'Acousticness', 'Speechiness', 'Positivity', 'Instrumentalness']

        except:
            return redirect(url_for('myMusic', _external=True))

        return render_template('info.html', t=tempo, l=loudness, id=track_id, p=track_popularity, labels=labels, data=audio_features, type=info_type)

    else:
        artist_id = id[:-1]
        artist_info = api_client.get_track_or_artist_info(artist_id, "artists")
        info_type="artist"

        followers = f"{artist_info['followers']:,d}"
        genres = artist_info['genres']
        name = artist_info['name']
        image = artist_info['image']
        popularity = artist_info['popularity']

        return render_template('info.html', f=followers, g=genres, n=name, i=image, p=popularity, type=info_type)


@app.route('/more')
def more():

    return configure_user_top('more.html', 30)


@app.route("/analytics")
def analytics():

    api_client = init_api_client()
    cols = ['danceability', 'energy', 'acousticness', 'speechiness', 'valence', 'instrumentalness']
    data_client = DataClient(api_client, session.get('time_frame'))
    
    request_data = api_client.get_user_info()
    user_info = request_data['user_info']
    username = user_info["display_name"]

    user_avg_track_popularity = data_client.get_user_avg_popularity("tracks")
    spotify_avg_popularity = data_client.get_spotify_charts_avg_popularity()
    print(spotify_avg_popularity)
    user_avg_artist_popularity = data_client.get_user_avg_popularity("tracks")

    user_avg_features = data_client.get_user_top_avg_audio_features(cols)
    spotify_avg_features = data_client.get_spotify_charts_avg_features(cols)

    return render_template('analytics.html', time=session.get("time_frame"), name=username, user_avg_features=user_avg_features, top_avg_features=spotify_avg_features)


@app.route("/new")
def new():

    return "my music taste is dogwater, help me find new tracks"


def init_api_client(): 
    
    oauth_info = session.get('oauth_info')
    start_time = session.get('start_time') #gets the time at which access_token was first given
    
    current_time = int(time.time()) #gets the time when this function is called
    token_expiry = oauth_info['expires_in']  #sets the token expiry time which is 3600 seconds or 1 hour
    time_diff = current_time - start_time #how much time has passed since token was given

    if (time_diff > token_expiry): #if more than an hour has passed, a new access_token will be provided
        new_token = oauth_client.refresh_token(oauth_info['refresh_token'])   #logic for refreshing access token
        start_time = int(time.time())

        return SpotifyApiClient(new_token['access_token'])
    
    else:
        return SpotifyApiClient(oauth_info['access_token'])


def configure_user_top(html_page, limit):

    api_client = init_api_client()
    time_frame = session.get('time_frame')

    try:
        user_top_tracks = api_client.get_user_top_info(limit, time_frame, "tracks")
        user_top_artists = api_client.get_user_top_info(limit, time_frame, "artists")

    except:
        return "Sorry your account is new and has no music data I can use :("

    songs = user_top_tracks['name']
    song_ids = user_top_tracks['id']
    song_covers = user_top_tracks['image']
    song_artists = user_top_tracks['trackartistname']
    song_albums = user_top_tracks['trackalbumname']

    artists = user_top_artists['name']
    artist_ids = user_top_artists['id']
    artist_covers = user_top_artists['image']

    return render_template(html_page, songs=songs, song_ids=song_ids, song_covers=song_covers, song_artists=song_artists, song_albums=song_albums, artists=artists, artist_ids=artist_ids, artist_covers=artist_covers, zip=zip, time=time_frame)


if __name__ == "__main__":
    app.run()