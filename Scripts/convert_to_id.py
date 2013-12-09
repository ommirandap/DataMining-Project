import json

origen = raw_input('Archivo Origen? ')
destino = raw_input('Archivo Destino? ')

source = open(origen,'r')
destiny = open(destino,'a')

new_tweet = {}

for line in source:
    tweet = json.loads(line)
    a = tweet.pop('id_str',None)
    new_tweet['str_id'] = a
    a = tweet.pop('connotacion', None)
    new_tweet['connotacion'] = a
    final_tweet = json.dumps(new_tweet)
    destiny.write(final_tweet)
    destiny.write('\n')

source.close()
destiny.close()
