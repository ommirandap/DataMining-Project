import json

origen = 'Debate-ANP.js'
destino = 'Debate-ANP-processed-textidtime.js'

source = open(origen,'r')
destiny = open(destino,'a')

new_tweet = {}

for line in source:
    tweet = json.loads(line)
    #a = tweet.pop('id_str', None)
    #new_tweet['str_id'] = a
    a = tweet.pop('user', None)
    a = a.pop('id_str', None)
    new_tweet['user'] = a
#    a = tweet.pop('text', None)
#    new_tweet['text'] = a
#    a = tweet.pop('created_at', None)
#    new_tweet['created_at'] = a
    final_tweet = json.dumps(new_tweet)
    destiny.write(final_tweet)
    destiny.write('\n')

source.close()
destiny.close()
