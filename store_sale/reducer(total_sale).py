#!/usr/bin/env python
import sys
	
a = 0
b = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
	        # Something has gone wrong. Skip this line.
        continue
	
    p,q = data_mapped
    p = float(p)
    q = float(q)
    a += p
    b += q
   
print a,b
    


