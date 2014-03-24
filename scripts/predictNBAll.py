#! /usr/bin/env python
import sys
import pickle
import pprint
from collections import defaultdict
from priorityNB import def_int,def_float

def product(xs):
    res = 1
    for x in xs:
      res = res * x
    return res

with open(sys.argv[2],"rb") as f:
  priority_count = pickle.load(f)
  priority_con_count = pickle.load(f)
  priority_mar_prob = pickle.load(f)
  priority_con_prob = pickle.load(f)


#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(priority_count)
#pp.pprint(priority_con_count)
#pp.pprint(priority_mar_prob)
#pp.pprint(priority_con_prob)

with open(sys.argv[1]) as data:
  for line in data.readlines()[1:]:
    items = line.strip().split(",")
    obs = items[0:4]
    probs = defaultdict(float)
    for pri in priority_mar_prob.keys():
      if(pri not in obs):
        probs[pri] = priority_mar_prob[pri] * product([priority_con_prob[pri][i] for i in obs])
    probs_sorted = sorted(probs.items(), key=lambda x:-x[1])
    print line.strip() +  "," + ",".join(x[0] for x in probs_sorted)
           
