#! /usr/bin/env python
import sys
from collections import defaultdict
onehit = defaultdict(int)
twohit = defaultdict(int)

with open(sys.argv[1]) as data:
  for line in data.readlines():
    items = line.strip().split(",")
    target = items[4:6]
    for i in range(2,12):
        hits=0
        preds =  items[6:6+i]
        for pred in preds:
            if pred in target: hits +=1
        if(hits==1): onehit[i] +=1
        if(hits==2): twohit[i] +=1


for i in range(2,10):
  print "onehit in top %d: %d" % (i,onehit[i])
  print "twohit in top %d: %d" % (i,twohit[i])
