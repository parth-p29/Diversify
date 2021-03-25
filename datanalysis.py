import pandas as pd
from retry.api import retry_call

class DataClient():

    def __init__(self, api_client, time_frame):
        
        self.api_client = api_client
        self.song_ids = api_client.get_user_top_info(50, time_frame, "tracks")['id']
        self.spotify_dataset = pd.read_csv('static/csv/2020_spotify.csv')
        self.csv_ids = ','.join(self.song_ids) 


    def get_user_top_avg_audio_features(self, columns):

        try:
            features_list = self.api_client.get_audio_features_for_multiple_songs(self.csv_ids)
    
        except:
            features_list = retry_call(self.api_client.get_audio_features_for_multiple_songs, fargs=[self.csv_ids])

        data_table = pd.DataFrame(features_list, columns=columns)
        avg_value_list = [round(data_table[col].mean(), 4) for col in columns]

        return avg_value_list


    def get_user_avg_popularity(self, popularity_type):

        try:
            popularity_list = self.api_client.get_multiple_track_or_artist_info(popularity_type, self.csv_ids)

        except:
            popularity_list = retry_call(self.api_client.get_multiple_track_or_artist_info, fargs=[popularity_type, self.csv_ids])

        data_table = pd.DataFrame(popularity_list, columns=['Popularity'])
        avg_pop = round(data_table['Popularity'].mean(), 2)
        
        return avg_pop


    def get_spotify_charts_avg_features(self, columns):
        
        avg_value_list = [round(self.spotify_dataset[col].mean(), 4) for col in columns]
        return avg_value_list


    def get_spotify_charts_avg_popularity(self):
        
        return self.spotify_dataset['popularity'].mean()


#useful functions
def get_user_top_data(data):

    df = pd.DataFrame(data.values())
    ls = df.to_dict("list")

    return ls
