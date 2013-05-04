import urllib
import json
import pprint

for p in range(10):
    response_json = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft&page=%d" % (p+1))
    response = json.load(response_json)
    #pprint.pprint(response)
    if 'results' in response:
        for tweet in response['results']:
            if 'text' in tweet:
                print tweet['text']
