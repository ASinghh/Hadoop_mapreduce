# -*- coding: utf-8 -*-


import sys

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
        print data[0]