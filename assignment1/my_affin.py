import json
from pprint import pprint
import re

def readAffinities(filename='AFINN-111.txt'):
  d = {}
  with open(filename) as f:
    for line in f:
      m = re.match(r'(.*)\t([+-]?\d+)', line)
      if m:
        d[m.group(1)] = int(m.group(2))
  return d

aff_of = readAffinities()

def getaffin(line):
    tweet = json.loads(line)
    if 'lang' in tweet and tweet['lang']=='en' and 'text' in tweet:
        text = tweet['text']
        aff_sum = 0
        for word in re.split(r'\s+', text):
            if word in aff_of:
                aff_sum += aff_of[word]
        return aff_sum
    return None
    #pprint(tweet)
