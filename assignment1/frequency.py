#!/usr/bin/env python

import sys
import json
import re
from collections import defaultdict

def tweetsFromFile(filename):
    with open(filename) as f:
        for line in f:
            yield json.loads(line)

def main():
    counter = defaultdict(int)
    for t in tweetsFromFile(sys.argv[1]):
        if 'text' in t:
            for w in t['text'].split():
                counter[w] += 1
    nterms = sum(counter.values())
    #print "Total", nterms, "versions of", len(counter.keys()),"terms."
    for w in counter.items(): #counter.most_common(100):
        print w[0].encode('utf-8'), float(w[1])/nterms #, float(counter[w]) / nterms

if __name__ == '__main__':
    main()
