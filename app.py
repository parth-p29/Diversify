from flask import Flask, render_template, url_for, redirect
from secrets import *
import requests
import json


app = Flask(__name__)

OAUTH_AUTHORIZE_URL= 'https://accounts.spotify.com/authorize'

auth_url = requests.get(OAUTH_AUTHORIZE_URL, params=payload).url



@app.route('/')
def index():

    return "<a href=" + auth_url + ">Login with Spotify</a>"


@app.route("/redirect/")
def redirectPage():

    return "fucking finally"

'''
if __name__ == "__main__":
    app.run(debug=True)
'''
#{"access_token": "BQDjTNtLuIwJNA6F33bgv7TX7RLJprC4GG8Ganbzc92GRtfarR6hRIDi2OIb3n0An1QyJQv8s6sh2Fl4wAv8IUuHaApoUqNmgjTDnfPhdp-DKf2YQwjwMO7iUjGToZoO3RtIWfWAJboPA_Y9Ke-lwJR2Gycu1S47DSevBnyjnMVmxaykXJjUhy67", "token_type": "Bearer", "expires_in": 3600, "refresh_token": "AQDuyF415GTx4qH-soq1s4Yt7ZSf-o5vq3Th-4J6N8treukVnjutUt4y85Y1nZqVdUlvgDfohk7yUyF337op24YsSJcugguiTJ_3IvVYDvlWbNHpJTeuymbSm17HTGHAiQs", "scope": "user-library-read user-top-read", "expires_at": 1614324258}