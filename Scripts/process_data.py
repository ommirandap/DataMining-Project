import json

origen = raw_input('Archivo Origen? ')
destino = raw_input('Archivo Destino? ')

source = open(origen,'r')
destiny = open(destino,'a')

for line in source:
    tweet = json.loads(line)
    tweet.pop('annotations',None)
    tweet.pop('contributors',None)
    tweet.pop('coordinates',None)
    tweet.pop('current_user_retweet',None)
    tweet.pop('favorite_count',None)
    tweet.pop('favorited',None)
    tweet.pop('filter level',None)
    tweet.pop('geo',None)
    tweet.pop('id',None)
    tweet.pop('in_reply_to_screen_name',None)
    tweet.pop('in_reply_to_status_id',None)
    tweet.pop('in_reply_to_status_id_str',None)
    tweet.pop('in_reply_to_user_id',None)
    tweet.pop('in_reply_to_user_id_str',None)
    tweet.pop('lang',None)
    tweet.pop('place',None)
    tweet.pop('possibly_sensitive',None)
    tweet.pop('scopes',None)
    tweet.pop('retweeted',None)
    tweet.pop('retweeted_status',None)
    tweet.pop('source',None)
    tweet.pop('truncated',None)
    tweet.pop('user',None)
    tweet.pop('withheld_copyright',None)
    tweet.pop('withheld_in_countries',None)
    tweet.pop('withheld_scope',None)
    tweet.pop('',None)
    tweet['entities'].pop('hashtags',None)
    tweet['entities'].pop('symbols',None)
    tweet['entities'].pop('urls',None)
    tweet['entities'].pop('media',None)
    for a in tweet['entities']['user_mentions']:
        a.pop('indices',None)
        a.pop('id',None)
        a.pop('name',None)
    final_tweet = json.dumps(tweet)
    destiny.write(final_tweet)
    destiny.write('\n')
    

source.close()
destiny.close()
