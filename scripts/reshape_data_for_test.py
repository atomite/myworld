#! /usr/bin/env python
import sys
pris = [str(i) for i in range(100,116)]
colnames = ",".join(pris)
print colnames
with open(sys.argv[1]) as data:
  for line in data.readlines()[1:]:
    items = line.strip().split(",")
    row = [ 'Y' if x in items[0:4] else 'N' for x in pris]
    print ",".join(row)
