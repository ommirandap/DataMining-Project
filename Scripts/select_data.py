import json

source = open('clean_tweets.js','r')
destiny = open('selected_tweets.js','a')
i = 0
a = input('Empezar desde linea?')

for line in source:
    if i == a:
        break
    i = i+1

for line in source:
    tweet = json.loads(line)
    print tweet['text']
    selector = raw_input('Sirve? (Y/N/exit)')
    if selector == 'Y':
        animo = raw_input('Connotacion? (Positivo/Negativo/Neutro)')
        tweet['connotacion'] = animo
        final_tweet = json.dumps(tweet)
        destiny.write(final_tweet)
        destiny.write('\n')
    if selector == 'exit':
        break
    i = i+1

print('Quedaste en la linea: '+str(i))

source.close()
destiny.close()
