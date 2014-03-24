#! /usr/bin/env python
import sys
import pickle
import pprint
from collections import defaultdict


def def_int():
    return defaultdict(int)


combos = [(1, 2, 3, 4), (1, 2, 3, 5), (1, 2, 3, 6), (1, 2, 4, 5), (1, 2, 4, 6), (1, 2, 5, 6), (1, 3, 4, 5),
          (1, 3, 4, 6), (1, 3, 5, 6), (1, 4, 5, 6), (2, 3, 4, 5), (2, 3, 4, 6), (2, 3, 5, 6), (2, 4, 5, 6),
          (3, 4, 5, 6)]
setof6 = set([1, 2, 3, 4, 5, 6])
count_total = defaultdict(int)
count_dict = defaultdict(def_int)
with open(sys.argv[1]) as data:
    for line in data.readlines()[1:]:
        items = line.strip().split(",")
        for combo in combos:
            key = ",".join([str(items[i - 1]) for i in combo])
            count_total[key] += 1
            for i in setof6 - set(combo):
                count_dict[key][items[i - 1]] += 1


with open(sys.argv[2],"w") as f1:
    for key in count_total.keys():
      f1.write(key+":"+str(count_total[key])+"\n")
with open(sys.argv[3],"w") as f2:
    for key in count_dict.keys():
        f2.write(key+": "+ ",".join(["%s:%d" % (k,v) for k,v in count_dict[key].items()])+"\n")

with open(sys.argv[4],"wb") as f:
  pickle.dump(count_total,f)
  pickle.dump(count_dict,f)





