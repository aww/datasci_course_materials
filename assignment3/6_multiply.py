#!/usr/bin/env python

import MapReduce
import sys
import collections

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
        for i in range(size):
            mr.emit_intermediate((row, i), (which, col, val))
    elif which == "b":
        for i in range(size):
            mr.emit_intermediate((i, col), (which, row, val))
    
def reducer(cell, idxval_list):
    # build index
    components = collections.defaultdict(list)
    for which, i, val in idxval_list:
        components[i].append(val)

    # Compute product
    sumprod = 0
    for i,val_list in components.items():
        if len(val_list) == 2:
            sumprod += val_list[0] * val_list[1]
        elif len(val_list) > 2:
            raise Exception("Term (%d, %d, %d) has more than 2 factors!" % (cell[0], cell[1], i))
    if sumprod != 0:
        mr.emit( (cell[0], cell[1], sumprod) )

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
