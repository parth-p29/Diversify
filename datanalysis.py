from spotifyapiclient import *
import pandas as pd
from retry.api import retry_call

def get_user_top_audio_features(api_client):

    #get Id's of user top songs
    short_term_songs = api_client.get_user_top_info(10, "short_term", "tracks")[1]
    medium_term_songs = api_client.get_user_top_info(40, "medium_term", "tracks")[1]
    long_term_songs = api_client.get_user_top_info(50, "long_term", "tracks")[1]
    all_songs = list(set(short_term_songs+medium_term_songs+long_term_songs)) #removes all duplicates

    csv_list = ','.join(all_songs)

    top_spotify_songs = pd.read_csv('static/csv/spotifytoptracks.csv')

    try:
        features_list = api_client.get_audio_features_for_multiple_songs(csv_list)
    
    except:
        features_list = retry_call(api_client.get_audio_features_for_multiple_songs, fargs=[csv_list])

    columns=['Danceability', 'Energy', 'acousticness', 'Speechiness', 'Valence', 'instrumentalness']
    data_table = pd.DataFrame(features_list, columns=columns)
    #data_table = pd.DataFrame(df_dict, index=['Danceability', 'Energy', 'acousticness', 'Speechiness', 'Valence', 'instrumentalness'])
    
    avg_value_list = []
    for col in columns:
        val = round(data_table[col].mean(), 2)
        avg_value_list.append(val)
        
    return (avg_value_list)

