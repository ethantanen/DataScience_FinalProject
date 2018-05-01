import tweepy
from flask_oauthlib.client import OAuth
from flask import Flask, redirect, url_for, session, request, jsonify


app = Flask(__name__)

oauth = OAuth()
oauth.init_app(app)

oauth = OAuth(app)

consumer_token = 'SQ1s4LlutS6JtWDyl1xRwuPRA'
consumer_secret = 'og0E2SOGXTSnkPQxqt4gGTUQBk5ZN0qPlkUosik90UJ91993ZV'

access_token = '544663361-0qlZ414jGrAm5SstL1kIp8vwBvkS2BXghno3muao'
access_token_secret = 'AsZdUOxeu0bDOfFEr8J7qBsT9VmX38yARLyxaneA0M0Uh'

auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

results = api.search(q="Flatbush")
for r in results:
    print(r.text)
