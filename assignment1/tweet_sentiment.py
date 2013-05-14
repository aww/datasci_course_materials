#!/usr/bin/env python

import sys
import json
import re
import pprint

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
        scoring_words = []
        unkown_words = []
        for word in tweet['text'].split():
            if word.lower() in mapping:
                sent += mapping[word.lower()]
        return sent
    else:
        return 0

def main():
    sentiment_mapping = sentimentMappingFromFile(sys.argv[1])
    for t in tweetsFromFile(sys.argv[2]):
        #pprint.pprint(t)
        print sentimentOfTweet(t, sentiment_mapping)

if __name__ == '__main__':
    main()
