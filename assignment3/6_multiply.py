#!/usr/bin/env python

import MapReduce
import sys

"""
Matrix multiply
"""
size = 5

mr = MapReduce.MapReduce()

def mapper(record):
    which = record[0]
    row = record[1]
    col = record[2]
    val = record[3]
    if which == "a":
        for i in range(5):
            mr.emit_intermediate((row, i), (col, val))
    elif which == "b":
        for i in range(5):
            mr.emit_intermediate((i, col), (row, val))
    
def reducer(cell, idxval_list):
    prod = 0
    # Form a list of values paired by index

    for idx, val in idxval_list:
        prod += val
    if prod != 0:
        mr.emit( (cell[0], cell[1], prod) )

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
