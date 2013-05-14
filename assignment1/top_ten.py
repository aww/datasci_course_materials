#!/usr/bin/env python

import sys
import json
import re
from collections import defaultdict
import pprint

def tweetsFromFile(filename):
    with open(filename) as f:
        for line in f:
            yield json.loads(line)

def main():
    counter = defaultdict(int)
    for t in tweetsFromFile(sys.argv[1]):
        #pprint.pprint(t)
        if 'entities' in t and 'hashtags' in t['entities']:
            for ht in t['entities']['hashtags']:
                 if 'text' in ht:
                     ht_text = ht['text']
                     #print ht_text
                     counter[ht_text] += 1
    ht_cnt_sorted = sorted(counter.items(), key=lambda x: x[1])
    for ht,cnt in ht_cnt_sorted[-10:]: #counter.most_common(100):
        print ht.encode('utf-8'), float(cnt)

if __name__ == '__main__':
    main()
