#!/usr/bin/env python
import sys

    # read standard input line by line
store = []
dic = {}
for line in sys.stdin:
    # strip off extra whitespace, split on tab and put the data in an array
    data = line.strip().split("\t")
    if len(data) != 6 :
        continue
        # This is the place you need to do some defensive programming
        # what if there are not exactly 6 fields in that line?
        # YOUR CODE HERE
        
        # this next line is called 'multiple assignment' in Python
        # this is not really necessary, we could access the data
        # with data[2] and data[5], but we do this for conveniency
        # and to make the code easier to read
    
    date, time, store, item, cost, payment = data
    cost = float(cost)
    
    
    if store not in dic:
        dic[store] = cost
    if dic[store]<= cost:
        dic[store] = cost
   
keys = list(dic.keys())
values = list(dic.values())
    
    
for i in range(len(keys)):
    
 #        Now print out the data that will be passed to the reducer
    print ("{0}\t{1}".format(keys[i], values[i]))

