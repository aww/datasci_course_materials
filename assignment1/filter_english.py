#!/usr/bin/env python

import json
import sys

if __name__ == '__main__':
    text_only = False
    filename = sys.argv[1]
    if sys.argv[1] == '-t':
        text_only = True
        filename = sys.argv[2]
    
    count = 0
    with open(filename) as f:
        for line in f:
            tweet = json.loads(line)
            if 'text' in tweet and 'lang' in tweet and tweet['lang'] == 'en':
                if text_only:
                    count += 1
                    print "%10d %s" % (count, tweet['text'].encode('utf-8'))
                else:
                    print line,
