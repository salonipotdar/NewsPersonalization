import os
import sys
from sets import Set
import numpy

fdata = open(sys.argv[1])
fout = open(sys.argv[2], "w")
output_type = int(sys.argv[3])

doc_set = Set()

user_ctr = {}
for line in fdata:
    line = line[:-1]
    line_arr = line.split("|")
    user_id = int(line_arr[1])
    shown_doc = line_arr[0].split(" ")[1]
    clicked = int(line_arr[0].split(" ")[2])
    doc_set.add(shown_doc)

    if user_id not in user_ctr:
        user_ctr[user_id] = {}
    if shown_doc not in user_ctr[user_id]:
        user_ctr[user_id][shown_doc] = [0,0]
    user_ctr[user_id][shown_doc][0] += 1
    if clicked:
        user_ctr[user_id][shown_doc][1] += 1

num_user = len(user_ctr)
sorted_docs = sorted(doc_set)
num_doc = len(sorted_docs)

if output_type == 5:
    #normalized ctr
    ctr = numpy.zeros((num_doc, num_user+1))
    for d in range(0, num_doc):
        for c in range(1, num_user+1):
            doc = sorted_docs[d]
            if doc not in user_ctr[c]:
                ctr[d][c] = 0 
            else:
                ctr[d][c] = float(user_ctr[c][doc][1]) / user_ctr[c][doc][0]
    output_string = ""
    for c in range(1, num_user+1):
        c_sum = 0.0
        for d in range(0, num_doc):
            c_sum += ctr[d][c]
        #for d in range(0, num_doc):
        #    ctr[d][c] /= c_sum
        if c_sum < 1e-6:
            continue
        output_string += str(c)
        for d in range(0, num_doc):
            output_string += " " + str(d+1) + ":" + str(ctr[d][c])
        output_string += "\n"
elif output_type == 4:
    #normalized show
    ctr = numpy.zeros((num_doc, num_user))
    for d in range(0, num_doc):
        for c in range(1, num_user+1):
            doc = sorted_docs[d]
            ctr[d][c] = user_ctr[c][doc][0]
    for c in range(0, num_user):
        c_sum = 0.0
        for d in range(0, num_doc):
            c_sum += ctr[d][c]
        for d in range(0, num_doc):
            ctr[d][c] /= float(c_sum)
    output_string = ""
    for d in range(0, num_doc):
        output_string += sorted_docs[d]
        for c in range(1, num_user+1):
            output_string += " " + str(ctr[d][c])
        output_string += "\n"
else:
    output_string = ""
    for c in range(1, num_user+1):
        output_string += str(c)
        for doc in sorted_docs:
            if output_type == 0:
                output_string += " " + str(user_ctr[c][doc][0])
            elif output_type == 1:
                output_string += " " + str(user_ctr[c][doc][1])
            elif output_type == 2:
                if doc not in user_ctr[c]:
                    output_string += " 0"
                else:
                    output_string += " " + str(float(user_ctr[c][doc][1]) / user_ctr[c][doc][0])
            elif output_type == 3:
                output_string += " " + str(user_ctr[c][doc][0]) + "," + str(user_ctr[c][doc][1]) + "," + str(float(user_ctr[c][doc][1]) / user_ctr[c][doc][0])
        output_string += "\n"

fout.write(output_string)
