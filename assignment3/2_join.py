#!/usr/bin/env python

import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

#
# We implement this join
#
# SELECT *
# FROM Orders, LineItem
# WHERE Order.order_id = LineItem.order_id

def mapper(record):
    table = record[0] # is "order" or "line_item"
    order_id = record[1]
    if table == "order" or table == "line_item":
        mr.emit_intermediate(order_id, record)

def reducer(key, list_of_values):
    orders = []
    line_items = []
    for record in list_of_values:
        if record[0] == "order":
            orders.append(record)
        elif record[0] == "line_item":
            line_items.append(record)
    for order in orders:
        for line_item in line_items:
            mr.emit(order + line_item)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
