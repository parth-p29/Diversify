# Diversify

## Inspiration

Diversify is a Spotify Analytics Web App that allows one to view all their music data and get to know information about their top songs/artists, listening habits, how "basic" their music taste is and even generating new music based on personal interests.

Having Spotify as my favourite music streaming platform and loving the concept of the "year wrapped," I wanted to make something similar which allowed me to see my data whenever I pleased. I also wanted to compare my top music choices with that of the top songs in a particular year to see how diverse the type of music I listend to was. 

This led me to creating Diversify. With this app, anyone can view their data and learn more about themselves and the music they listen too. They can also find new songs based on their own interests or go crazy and build random playlists for any mood! 

## Built With

- [Flask](https://flask.palletsprojects.com/en/1.1.x/): Web framework used for setting up the app

- [Spotify Web API](https://developer.spotify.com/documentation/web-api/): Used to retrieving user data

- [Python (Requests)](https://docs.python-requests.org/en/master/): Used for sending requests to the Spotify Web API with Python

- [Pandas](https://pandas.pydata.org/): Used for manipulating data and calculating various values such as the user's basic score, lisenting habits etc.

- [Azure](https://azure.microsoft.com/en-ca/services/cognitive-services/text-analytics/): Cloud Service used for performing Sentiment Analysis on song lyrics

- [Lyrics OVH](https://lyricsovh.docs.apiary.io/#reference/0/lyrics-of-a-song/search): API used to retrieve song lyrics

- [Chart.js](https://www.chartjs.org/docs/latest/): Used for visualing user data on various graphs inluding: bar, radar, doughnut etc.

- [Spotify Datasets](https://www.kaggle.com/atillacolak/top-50-spotify-tracks-2020): Used to compare with the user data

## Getting Started

If you want to just use the finished web app, please skip to the "Usage" header. If you want to integrate my apis into your own projects then follow these steps:

1. git clone
