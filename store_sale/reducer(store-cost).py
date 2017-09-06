#!/usr/bin/env python
import sys
	
dic = {}
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
	        # Something has gone wrong. Skip this line.
        continue
	
    k,s = data_mapped
    s = float(s)
    if k not in dic:
        dic[k] = s
    if dic[k]<= s:
        dic[k] = s
   
keys = list(dic.keys())
values = list(dic.values())



	
for i in range(len(keys)):
    print(keys[i],    values[i])
    


