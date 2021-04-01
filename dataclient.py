import pandas as pd
from retry.api import retry_call
import statistics
from collections import Counter

class DataClient():

    def __init__(self, api_client, time_frame):
        
        self.api_client = api_client
        self.spotify_dataset = pd.read_csv('static/csv/spotifytoptracks.csv')
        self.ids = {
            "artists": (','.join(api_client.get_user_top_info(33, time_frame, "artists")['id'])),
            "tracks": (','.join(api_client.get_user_top_info(50, time_frame, "tracks")['id'])) 
        }

    def get_user_top_avg_audio_features(self, columns):

        try:
            features_list = self.api_client.get_audio_features_for_multiple_songs(self.ids['tracks'])
    
        except:
            features_list = retry_call(self.api_client.get_audio_features_for_multiple_songs, fargs=[self.ids['tracks']])

        data_table = pd.DataFrame(features_list, columns=columns)
        avg_value_list = [round(data_table[col].mean(), 4) for col in columns]

        return avg_value_list

    def get_user_avg_popularity(self, popularity_type):

        try:
            popularity_list = self.api_client.get_multiple_track_or_artist_info(popularity_type, self.ids[popularity_type], "popularity")

        except:
            popularity_list = retry_call(self.api_client.get_multiple_track_or_artist_info, fargs=[popularity_type, self.ids[popularity_type], "popularity"])

        data_table = pd.DataFrame(popularity_list, columns=['Popularity'])

        return round(data_table['Popularity'].mean(), 2)

    def get_spotify_charts_avg_features(self, columns):
        
        avg_value_list = [round(self.spotify_dataset[col.lower()].mean(), 4) for col in columns]
        return avg_value_list

    def get_spotify_charts_avg_popularity(self):

        output_dict = lambda **data: data

        track_ids = ','.join(self.spotify_dataset['track_id'].to_list())
        artist_ids = ','.join(self.api_client.find_artists_from_songs(track_ids))

        track_popularity = self.api_client.get_multiple_track_or_artist_info("tracks", track_ids, "popularity")
        artist_popularity = self.api_client.get_multiple_track_or_artist_info("artists", artist_ids, "popularity")

        return output_dict(track=statistics.mean(track_popularity), artist=statistics.mean(artist_popularity))

    def get_user_top_genres(self):
        
        genres = {}
        top_artist_genres = self.api_client.get_multiple_track_or_artist_info("artists", self.ids['artists'], "genres")

        for artist_genres in top_artist_genres:

            for genre in artist_genres:

                if genre in genres.keys():
                    genres[genre] += 1

                else:
                    genres[genre] = 1

        top_genres = dict(Counter(genres).most_common(5)) 

        return (list(top_genres))

    def get_similarity_between_features(self, user, spotify):

        percent_list = [round(((min(item1, item2) / max(item1,item2)) * 100), 2) for item1, item2 in zip(user, spotify)]
        
        return percent_list

#useful functions
def get_user_top_data(data):

    df = pd.DataFrame(data.values())
    ls = df.to_dict("list")

    return ls
