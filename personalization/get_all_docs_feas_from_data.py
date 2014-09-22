import os
import sys
from sets import Set

ftrainfile = open(sys.argv[1])
fout = open(sys.argv[2], "w")

docs = Set()
for line in ftrainfile:
    line = line[:-1]
    line_arr = line.split("|")
    for i in range(2, len(line_arr)):
        docs.add(line_arr[i].strip(' '))

sorted_docs = sorted(docs)

for doc in sorted_docs:
    fout.write("%s\n"% doc)
