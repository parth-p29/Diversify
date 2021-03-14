from spotifyapiclient import *
import pandas as pd
from retry.api import retry_call

def get_user_top_audio_features(api_client, columns):

    #get Id's of user top songs
    short_term_songs = api_client.get_user_top_info(20, "short_term", "tracks")[1]
    medium_term_songs = api_client.get_user_top_info(30, "medium_term", "tracks")[1]
    long_term_songs = api_client.get_user_top_info(50, "long_term", "tracks")[1]
    all_songs = list(set(short_term_songs+medium_term_songs+long_term_songs)) #removes all duplicates

    csv_list = ','.join(all_songs) 

    try:
        features_list = api_client.get_audio_features_for_multiple_songs(csv_list)
 
    except:
        features_list = retry_call(api_client.get_audio_features_for_multiple_songs, fargs=[csv_list])
          
    data_table = pd.DataFrame(features_list, columns=columns)
    
    avg_value_list = []
    for col in columns:
        val = round(data_table[col].mean(), 4)
        avg_value_list.append(val)
        
    return (avg_value_list)

def get_spotify_top_charts_data(columns):

    #utilize spotify top songs dataset
    data_table = pd.read_csv('static/csv/1930-2021.csv', usecols = columns)
    
    avg_value_list = []
    for col in columns:
        val = round(data_table[col].mean(), 4)
        avg_value_list.append(val)
        
    return (avg_value_list)

