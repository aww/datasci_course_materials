#!/usr/bin/env python

import MapReduce
import sys

"""
Trim the last 10 characters from the DNA sequences and them return unique list
"""

mr = MapReduce.MapReduce()

def mapper(record):
    sequence = record[1]
    mr.emit_intermediate(sequence[:-10], 0)
    
def reducer(trimmed_sequence, dumby):
    mr.emit(trimmed_sequence)

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
