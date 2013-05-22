#!/usr/bin/env python

import MapReduce
import sys

"""
Friend counter
"""

mr = MapReduce.MapReduce()

def mapper(record):
    person = record[0] # is "order" or "line_item"
    friend = record[1]
    mr.emit_intermediate(person, 1)

def reducer(person, friend_counts):
    mr.emit( (person, sum(friend_counts)) )

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
