# input: training_data, cluster_data with each user to each cluster, output datafile
import os
import sys
from sets import Set
import numpy

fdata = open(sys.argv[1])
fcluster = open(sys.argv[2])
fout = open(sys.argv[3], "w")
output_type = int(sys.argv[4])

uid_cid = {}
for line in fcluster:
    uid = int(line.split(" ")[0])
    cid = int(line.split(" ")[1])
    uid_cid[uid] = cid

doc_set = Set()

cluster_ctr = {}
for line in fdata:
    line = line[:-1]
    line_arr = line.split("|")
    user_id = int(line_arr[1])
    if user_id not in uid_cid:
        continue
    cluster_id = uid_cid[user_id]
    shown_doc = line_arr[0].split(" ")[1]
    clicked = int(line_arr[0].split(" ")[2])
    doc_set.add(shown_doc)

    if cluster_id not in cluster_ctr:
        cluster_ctr[cluster_id] = {}
    if shown_doc not in cluster_ctr[cluster_id]:
        cluster_ctr[cluster_id][shown_doc] = [0,0]
    cluster_ctr[cluster_id][shown_doc][0] += 1
    if clicked:
        cluster_ctr[cluster_id][shown_doc][1] += 1

num_cluster = len(cluster_ctr)
sorted_docs = sorted(doc_set)
num_doc = len(sorted_docs)

if output_type == 5:
    #normalized ctr
    ctr = numpy.zeros((num_doc, num_cluster))
    for d in range(0, num_doc):
        for c in range(0, num_cluster):
            doc = sorted_docs[d]
            if doc not in cluster_ctr[c]:
                ctr[d][c] = 0
            else:
                ctr[d][c] = float(cluster_ctr[c][doc][1]) / cluster_ctr[c][doc][0]
    for c in range(0, num_cluster):
        c_sum = 0.0
        for d in range(0, num_doc):
            c_sum += ctr[d][c]
        for d in range(0, num_doc):
            ctr[d][c] /= c_sum
    output_string = ""
    for d in range(0, num_doc):
        output_string += sorted_docs[d]
        for c in range(0, num_cluster):
            output_string += " " + str(ctr[d][c])
        output_string += "\n"
elif output_type == 4:
    #normalized show
    ctr = numpy.zeros((num_doc, num_cluster))
    for d in range(0, num_doc):
        for c in range(0, num_cluster):
            doc = sorted_docs[d]
            ctr[d][c] = cluster_ctr[c][doc][0]
    for c in range(0, num_cluster):
        c_sum = 0.0
        for d in range(0, num_doc):
            c_sum += ctr[d][c]
        for d in range(0, num_doc):
            ctr[d][c] /= float(c_sum)
    output_string = ""
    for d in range(0, num_doc):
        output_string += sorted_docs[d]
        for c in range(0, num_cluster):
            output_string += " " + str(ctr[d][c])
        output_string += "\n"
else:
    output_string = ""
    for doc in sorted_docs:
        output_string += doc
        for c in range(0, num_cluster):
            if output_type == 0:
                output_string += " " + str(cluster_ctr[c][doc][0])
            elif output_type == 1:
                output_string += " " + str(cluster_ctr[c][doc][1])
            elif output_type == 2:
                if doc not in cluster_ctr[c]:
                    output_string += " 0"
                else:
                    output_string += " " + str(float(cluster_ctr[c][doc][1]) / cluster_ctr[c][doc][0])
            elif output_type == 3:
                output_string += " " + str(cluster_ctr[c][doc][0]) + "," + str(cluster_ctr[c][doc][1]) + "," + str(float(cluster_ctr[c][doc][1]) / cluster_ctr[c][doc][0])
        output_string += "\n"

fout.write(output_string)
