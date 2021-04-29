# Diversify
![Diversify (2)](https://user-images.githubusercontent.com/69891859/115304417-f2455980-a132-11eb-9532-1f7d4963e4e9.gif)


## Inspiration

Diversify is a Spotify analytics web app that allows one to view all their music data and get to know information about their top songs/artists, listening habits, how "basic" their music taste is and even generating new music based on personal interests.

Having Spotify as my favourite music streaming platform and loving the concept of the "year wrapped," I wanted to make something similar which allowed me to see my data whenever I pleased. I also wanted to compare my top music choices with that of the top songs in a particular year to see how diverse the type of music I listend to was. 

This led me to creating Diversify. With this app, anyone can view their data and learn more about themselves and the music they listen too. They can also find new songs based on their own interests or go crazy and build random playlists for any mood! 

## Built With

- [Flask](https://flask.palletsprojects.com/en/1.1.x/): Web framework used for setting up the app

- [Spotify Web API](https://developer.spotify.com/documentation/web-api/): Used to retrieve user data

- [Python (Requests)](https://docs.python-requests.org/en/master/): Used for sending requests to the Spotify Web API with Python

- [Pandas](https://pandas.pydata.org/): Used for manipulating data

- [Azure](https://azure.microsoft.com/en-ca/services/cognitive-services/text-analytics/): Cloud Service used for performing Sentiment Analysis on song lyrics

- [Lyrics OVH](https://lyricsovh.docs.apiary.io/#reference/0/lyrics-of-a-song/search): API used to retrieve song lyrics

- [Chart.js](https://www.chartjs.org/docs/latest/): Used for visualing user data on various graphs including: bar, radar, doughnut etc.

- [Kaggle Datasets](https://www.kaggle.com/atillacolak/top-50-spotify-tracks-2020): Used to compare user data with the top Spotify songs in 2020

- [Heroku](https://dashboard.heroku.com/apps): Platform used to deploy the app

## Getting Started

If you want to just use the finished web app, please skip to the **"Usage"** header. If you want to integrate my APIs into your own projects then follow these steps:

1. Go to the directory you want in your command line and write: 

        git clone https://github.com/parth-p29/Diversify.git
        
3. Next write the following to install all dependencies: 

        pip install -r requirements.txt
        
4. Create a [Spotify Dev account](https://developer.spotify.com/dashboard/login) and make a project so you can get 3 credentials: Client ID, Client Secret and Redirect URI
5. Traverse to **"oauth.py"** file and place in your values here:

        self.CLIENT_ID = "YOUR CLIENT ID"
        self.CLIENT_SECRET = "YOUR CLIENT SECRET"
        self.REDIRECT_URI = "YOUR REDIRECT URI"

6. You can use my **OauthClient class** to authorize with the Spotify API and use my various tools as you need!
7. [Optional] if you want to use the sentiment analysis feature, create an [Azure](https://azure.microsoft.com/en-us/free/) account and make a "Text Analytics" resource group
8. Find the **"azureclient.py"** file and place the Key and Endpoint provided in Azure here:

            self.client = TextAnalyticsClient(
            endpoint="YOUR AZURE ENDPOINT",
            credential=AzureKeyCredential("YOUR AZURE KEY CREDENTIALS"))

## Usage
    
You can access the web app [here](https://diversify-application.herokuapp.com/)

You will first be greeted to login with your Spotify account and authorize the app to have access to some of your data.

Once logged in, you can see your profile and the navigation bar with 3 other tabs you can access:

![profile page](https://user-images.githubusercontent.com/69891859/114288135-d1964900-9a3a-11eb-8f9e-4563268128bc.png)

The other 3 tabs take you to the **"My Music"**, **"Analytics"** and **"Recommendations"** pages. In the My Music page, you can see your top songs/artists in 3 different time frames (recent, 6 months and all time).

You can also click on the songs/artists and see more specific information about them. For the songs, you can see how popular they are, specific details about their audio, their lyrics and even a sentiment analysis describing how positive, negative or neutral the song is. For example:


![infopage pt1](https://user-images.githubusercontent.com/69891859/114288382-5d10d980-9a3d-11eb-8cfd-064fe71549f9.png)

![infopage audio analysis](https://user-images.githubusercontent.com/69891859/114288412-c1cc3400-9a3d-11eb-9e1c-79d58aea6280.png)

![infopage lyrical analysis](https://user-images.githubusercontent.com/69891859/114288423-d9a3b800-9a3d-11eb-87af-b50a783f4b44.png)

In the analytics page, you can see the analyzed history of your Spotify data such as: the audio features of the top songs you listen to, how popular your songs/artists are and also compare that with the most popular songs on Spotify. You can also get to know your most prominent genres and see an overall score depicting how your music taste compares with the public:

![basic score](https://user-images.githubusercontent.com/69891859/114288481-48811100-9a3e-11eb-9f6b-a439945aeccd.png)

On the recommendations page, using all the data collected and analyzed, a list of a couple songs and artists is produced that you will potentially enjoy. To test them out, you can even click on them to hear the songs and see its features to better judge if you want to add it to your playlists. 

If you want to just randomly make interesting playlists with differnt features such as: a party playlist or a chill playlist, there is also a tool that allows you to do that:

![recommendation creator](https://user-images.githubusercontent.com/69891859/114288583-466b8200-9a3f-11eb-9b20-b00e6db93323.png)

You can adjust the various sliders to produce different songs. The songs produced will still be aligned to your interests but with your customized audio features!

## Authors

- **Parth Patel** - [parth-p29](https://github.com/parth-p29)

