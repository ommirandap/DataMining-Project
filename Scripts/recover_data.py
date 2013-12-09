import json
import requests
from requests_oauthlib import OAuth1
import sys

API_KEY = 'VLvAAjdstV6v3VqbngNaQ'
API_SECRET = 'ex7GWIJhhVQCszbcncquVog6sIHi7XJy1rNC51ulV4'
USER_TOKEN = '10877162-atYMD05l0oSmHGKpCAn87mWawRbSTbmchTlO3LIg'
USER_SECRET = 'A4KSk6V7j0xhlOhI0tI3FoWKuOrmwMaHFcmVvApR2dI'

auth = OAuth1(API_KEY, API_SECRET, USER_TOKEN, USER_SECRET)

def get_tweet(id=None):
	url = 'https://api.twitter.com/1.1/statuses/show.json?id=' + id
	response = requests.get(url, auth=auth)
	return response

file_in = sys.argv[1]
file_out = 'Recovered-' + file_in
a = open(file_in,'r')
b = open(file_out,'a')

for ids in a:
	tweet_id = json.loads(ids)
	tweet_id = tweet_id['id_str']
	complete_tweet = get_tweet(tweet_id)
	b.write(complete_tweet.content)
	b.write('\n')
	print('iteracion lista')

a.close()
b.close()


