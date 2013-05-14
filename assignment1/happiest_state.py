#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
import re
from pprint import pprint
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

state_names = {
    'Alabama': 'AL',
    'Alaska ': 'AK',
    'Arizona ': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin ': 'WI',
    'Wyoming': 'WY',
}


def findStateFromName(str):
    m = re.match(r'.*,?\s+(\w\w)', str)
    if m:
        state_code_candidate = m.group(1).upper()
        if state_code_candidate in state_names.values():
            return state_code_candidate
    # Try to find things like 'New York, New York' and 'florida'
    # What about 'Kansas City', might map to KS but may be MO?
    return None

debug = 0

def findState(t):
    coord = None
    geo = None
    place = None
    user_location = None
    if u'coordinates' in t:
        coord = t[u'coordinates']
    if u'geo' in t:
        geo = t[u'geo']
    if u'place' in t:
        place = t[u'place']
    if u'user' in t and u'location' in t[u'user']:
        user_location = t[u'user'][u'location']
    if debug > 2:
        print '---'
        pprint(coord)
        pprint(geo)
        pprint(place)
        pprint(user_location)
    if place and u'full_name' in place:
        code = findStateFromName(place[u'full_name'])
        if code:
            return code
    return None
    
def main():
    sentiment_mapping = sentimentMappingFromFile(sys.argv[1])
    total_state_sentiment = defaultdict(lambda: [0,0])
    for t in tweetsFromFile(sys.argv[2]):
        #pprint.pprint(t)
        state = findState(t)
        if state:
            if debug > 1:
                print state
            (s,scoring,unknown) = sentimentOfTweet(t, sentiment_mapping)
            total_state_sentiment[state][0] += s
            total_state_sentiment[state][1] += 1

    sentiment_sorted_states = sorted(total_state_sentiment.items(), key=lambda x: float(x[1][0]) / float(x[1][1]))
    if debug > 0:
        for result in sentiment_sorted_states:
            #if result[1][1] < 5: continue # look at just the more popular words
            print "%s %5.2f %5d" % (result[0], float(result[1][0]) / float(result[1][1]), result[1][1])
    print sentiment_sorted_states[-1][0]

if __name__ == '__main__':
    main()
