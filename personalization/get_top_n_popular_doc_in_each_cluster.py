#input should be ydata-fp-td-clicks-v1_0.20090501.cluster_ctr_t2
#that is the output of ctr_per_cluster.py

import sys
import os
import numpy
import operator
from sets import Set

f = open(sys.argv[1])
top_n_start = int(sys.argv[2])
top_n_end = int(sys.argv[3])
fout = open(sys.argv[4], "w")

data = []
docs = []
for line in f:
    line = line[:-1]
    line_arr = line.split(" ")
    docs.append(line_arr[0])
    line = []
    for i in range(1, len(line_arr)):
        line.append(float(line_arr[i]))
    data.append(line)

num_docs = len(docs)
num_cluster = len(data[0])
uniq_top_n_doc = Set()
for i in range(0, num_cluster):
    to_be_sorted = {}
    for d in range(0, num_docs):
        to_be_sorted[docs[d]] = data[d][i]
    sorted_docs = sorted(to_be_sorted.iteritems(), key=operator.itemgetter(1))
    top_n_docs = []
    #top_n_docs.append(sorted_docs[0][0])
    #uniq_top_n_doc.add(sorted_docs[0][0])
    # output_string = "%s" % sorted_docs[0][0]
    for j in range(top_n_start, top_n_end):
        #output_string += " %s" % sorted_docs[j][0]
        top_n_docs.append(sorted_docs[j][0])
        uniq_top_n_doc.add(sorted_docs[j][0])
    top_n_docs = sorted(top_n_docs)
    fout.write("%s\n" % " ".join(top_n_docs))

fout.write("uniq: %s\n" % " ".join(uniq_top_n_doc))
print len(uniq_top_n_doc)
