from flask import Flask, render_template, url_for, redirect,request
from ouath import *
from spotifyapiclient import *
import requests
import json


app = Flask(__name__)

ouath_client = SpotifyOuathClient()
api_client = SpotifyApiClient()

@app.route('/')
def index():

    auth_url = ouath_client.get_auth_url()
    return render_template("index.html", url=auth_url)


@app.route("/redirect/")
def redirectPage():
    
    auth_code = request.args.get('code')
    response = ouath_client.get_auth_and_refresh_tokens(auth_code)
    access_token = response["access_token"]
    refresh_token = response["refresh_token"]

    USER_INFO = api_client.get_user_info(access_token)
    
    
    return USER_INFO


if __name__ == "__main__":
    app.run()










#{"access_token": "BQDjTNtLuIwJNA6F33bgv7TX7RLJprC4GG8Ganbzc92GRtfarR6hRIDi2OIb3n0An1QyJQv8s6sh2Fl4wAv8IUuHaApoUqNmgjTDnfPhdp-DKf2YQwjwMO7iUjGToZoO3RtIWfWAJboPA_Y9Ke-lwJR2Gycu1S47DSevBnyjnMVmxaykXJjUhy67", "token_type": "Bearer", "expires_in": 3600, "refresh_token": "AQDuyF415GTx4qH-soq1s4Yt7ZSf-o5vq3Th-4J6N8treukVnjutUt4y85Y1nZqVdUlvgDfohk7yUyF337op24YsSJcugguiTJ_3IvVYDvlWbNHpJTeuymbSm17HTGHAiQs", "scope": "user-library-read user-top-read", "expires_at": 1614324258}