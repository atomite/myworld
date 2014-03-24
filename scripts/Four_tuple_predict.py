#! /usr/bin/env python
import sys
import pickle
from collections import defaultdict
def def_int():
    return defaultdict(int)

with open(sys.argv[2],"rb") as f:
  count_total = pickle.load(f)
  count_dict = pickle.load(f)

with open(sys.argv[1]) as data:
  for line in data.readlines()[1:]:
    items = line.strip().split(",")
    obs = items[0:4]
    key = ",".join(obs)
    print line.strip() + "," + ",".join([y[0] for y in sorted(count_dict[key].items(),key=lambda x:x[1], reverse=True)])
