#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
import re
import pprint
from collections import defaultdict

def lines(fp):
    print str(len(fp.readlines()))

def sentimentMappingFromFile(filename):
    sentiments = {}
    with open(filename) as f:
        for line in f:
            m = re.match(r'(.*)\t(-?\d)', line)
            if m:
                sentiments[m.group(1)] = int(m.group(2))
            else:
                print "Warning: can't parse", line
    return sentiments

def tweetsFromFile(filename):
    with open(filename) as f:
        for line in f:
            yield json.loads(line)

def sentimentOfTweet(tweet, mapping):
    if 'text' in tweet:
        sent = 0
        scoring_words = set()
        unknown_words = set()
        for word in tweet['text'].split():
            sanetized_word = word
            sanetized_word = re.sub(u'^[(“"\']*',   '', sanetized_word)
            sanetized_word = re.sub(u'[:.?!),”"\']*$', '', sanetized_word)
            if sanetized_word.lower() in mapping:
                sent += mapping[sanetized_word.lower()]
                scoring_words.add(sanetized_word)
            else:
                unknown_words.add(sanetized_word)
        return (sent, scoring_words, unknown_words)
    else:
        return (0, [], [])

def main():
    sentiment_mapping = sentimentMappingFromFile(sys.argv[1])
    total_sentiment = defaultdict(lambda: [0, 0])
    for t in tweetsFromFile(sys.argv[2]):
        #pprint.pprint(t)
        (s,scoring,unknown) = sentimentOfTweet(t, sentiment_mapping)
        for w in unknown:
            total_sentiment[w][0] += s
            total_sentiment[w][1] += 1
    for result in sorted(total_sentiment.items(), key=lambda x: float(x[1][0]) / float(x[1][1])):
        #if result[1][1] < 5: continue # look at just the more popular words
        print result[0].encode('utf-8'), float(result[1][0]) / float(result[1][1])

if __name__ == '__main__':
    main()
