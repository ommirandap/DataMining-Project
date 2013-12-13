import json
import sys

input_filename = sys.argv[1]
output_filename = 'ID-time-' + input_filename 

input_stream = open(input_filename,'r')
output_stream = open(output_filename,'a')

aux_tweet = {}

for line in input_stream:
    tweet = json.loads(line)
    aux = tweet.pop('user', None)
    aux2 = aux.pop('id_str', None)
    aux_tweet['user_id'] = aux2
    aux = tweet.pop('created_at', None)
    aux_tweet['created_at'] = aux
    aux = tweet.pop('id_str', None)
    aux_tweet['id_str'] = aux
    
    final_tweet = json.dumps(aux_tweet)
    output_stream.write(final_tweet)
    output_stream.write('\n')

input_stream.close()
output_stream.close()