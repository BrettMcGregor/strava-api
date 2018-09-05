from stravalib.client import Client
# from httplib2 import Http
import requests
import webbrowser
# from urllib.parse import urlparse

client_id = '28201'
scope = None
client_secret = open('client.secret').read().split(",")[1]
redirect_uri = 'http://localhost'
auth_url = 'https://www.strava.com/oauth/authorize'
token_url = 'https://www.strava.com/oauth/token'


client = Client()
url = client.authorization_url(client_id, redirect_uri=redirect_uri, scope=None)

# send request to authorization url
# get the redirect url
# send request to it and get the full callback URL
# then parse to get the code

response = requests.get(url, {'approval_prompt': 'force'}, allow_redirects=True)
with open('strava_response', 'w') as file:
    for r in response.history:
        print(r.history, r.url, file=file)

webbrowser.open(response.history[0].url)

code = '760bbdf9a15a6f58bbe63da1db64b0f1343d6051' # get the code from the redirect url
access_token = client.exchange_code_for_token(client_id=client_id, client_secret=client_secret, code=code)

client.access_token = access_token
activity = client.get_activity(1817761172)
print(activity)
