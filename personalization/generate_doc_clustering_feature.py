#the input is the output of get_all_docs_feas_from_data.py
#read the doc features and do scaling
from sklearn import preprocessing
import numpy as np
import sys
import os

num_features = 5 #number of features without bias feature

f = open(sys.argv[1])
fout = open(sys.argv[2], "w")

data = []
for line in f:
    line = line[:-1]
    data.append(line)

npdata = np.zeros((len(data), num_features+1))
doc_id = []
for i in range(0, len(data)):
    line_arr = data[i].split(" ")
    doc_id.append(line_arr[0])
    npdata[i, 0] = 1 # bias
    if len(line_arr) < num_features:
        continue
    for j in range(1, num_features+1):
        value = line_arr[j].split(":")
        npdata[i, j] = float(value[1])

#npdata_scaled = preprocessing.scale(npdata)
npdata_scaled = npdata

for i in range(0, len(doc_id)):
    output_string = doc_id[i] + " 1:1"
    for j in range(1, num_features+1):
        output_string += " %d:%g" % (j+1, npdata_scaled[i, j])
    output_string += "\n"
    fout.write(output_string)
