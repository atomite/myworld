#! /usr/bin/env python
import sys
import pickle
import pprint
from collections import defaultdict

def def_int():
  return defaultdict(int)
def def_float():
  return defaultdict(float)
priority_count = defaultdict(int)
priority_con_count = defaultdict(def_int)
priority_mar_prob = defaultdict(float)
priority_con_prob = defaultdict(def_float)

total = 0

with open(sys.argv[1]) as data:
  for line in data.readlines()[1:]:
    items = line.strip().split(",")
    total += 1
    for pri1 in items:
      priority_count[pri1] += 1
      for pri2 in items:
        if pri2 != pri1: 
          priority_con_count[pri1][pri2] += 1;

for pri1 in priority_count:
  priority_mar_prob[pri1] = (0.0 + priority_count[pri1])/total
  for pri2 in priority_con_count[pri1]:
    priority_con_prob[pri1][pri2] = (0.0 + priority_con_count[pri1][pri2])/(priority_count[pri1]+0.01)

pp = pprint.PrettyPrinter(indent=4)

pp.pprint(priority_count)
pp.pprint(priority_con_count)
pp.pprint(priority_mar_prob)
pp.pprint(priority_con_prob)

with open(sys.argv[2],"wb") as f:
  pickle.dump(priority_count,f)
  pickle.dump(priority_con_count,f)
  pickle.dump(priority_mar_prob,f)
  pickle.dump(priority_con_prob,f)
