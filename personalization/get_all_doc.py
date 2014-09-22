#get all the doc and doc features
#input training_data

import sys
import os
from sets import Set
docs = Set()
f = open(sys.argv[1])
fout = open(sys.argv[2], "w")
for line in f:
    line = line[:-1]
    line_arr = line.split("|")
    for i in range(2, len(line_arr)):
        docs.add(line_arr[i].strip(' '))
sorted_docs = sorted(docs)
for doc in sorted_docs:
    fout.write(doc+"\n")

