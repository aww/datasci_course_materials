#!/usr/bin/env python

import sys
import json
import pprint
import collections

def loadFile(file):
    with open(file) as f:
        d = collections.defaultdict(list)
        for line in f:
            tmp = json.loads(line)
            d[tmp[0]].append(tmp[1])
    return d

def compare(file1, file2):
    d1 = loadFile(file1)
    d2 = loadFile(file2)
    k1 = set(d1.keys())
    k2 = set(d2.keys())
    print "Comparing %d keys to %d keys." % (len(k1), len(k2))

    only1 = k1 - k2
    only2 = k2 - k1
    both = k1 & k2

    isPassing = True
    if only1:
        print "Keys only in first:"
        pprint.pprint(only1)
        isPassing = False
    if only2:
        print "Keys only in second:"
        pprint.pprint(only2)
        isPassing = False
    if both:
        for k in both:
            if d1[k] != d1[k]:
                print "Values for key", k, "differ."
                isPassing = False
    if isPassing:
        print "SAME!"


if __name__ == '__main__':
    if len(sys.argv) > 2:
        compare(sys.argv[1], sys.argv[2])
    else:
        print "Usage:", sys.argv[0], "<file1.json> <file2.json>"
