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

input_filename = sys.argv[1]
input_stream = open(input_filename,'r')

output_filename = 'Recovered-' + input_filename
output_file = open(output_filename,'a')

for ids in input_stream:
	tweet_id = json.loads(ids)
	tweet_id = tweet_id['id_str']
	full_tweet = get_tweet(tweet_id)
	output_file.write(full_tweet.content)
	output_file.write('\n')

input_stream.close()
output_file.close()


