#!/usr/bin/env python

import MapReduce
import sys

"""
List asymmetric friendships
"""

mr = MapReduce.MapReduce()

def mapper(record):
    person = record[0]
    friend = record[1]
    if person < friend: # pair in a canonical (lexigraphic) way.
        mr.emit_intermediate((person,friend), '>')
    else:
        mr.emit_intermediate((friend,person), '<')
    
def reducer(pair, friendship_directions):
    if '>' in friendship_directions:
        if '<' in friendship_directions:
            pass # symmetric friendship
        else:
            mr.emit( pair )
            mr.emit( (pair[1], pair[0]) )
    else:
        if '<' in friendship_directions:
            mr.emit( pair )
            mr.emit( (pair[1], pair[0]) )
        else:
            pass # this shouldn't happen

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
