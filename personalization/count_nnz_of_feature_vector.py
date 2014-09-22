# count the number of non-zero of each instance
# input is the cluster training data, that is the feature file
import os
import sys

infile = open(sys.argv[1])
outfile = open(sys.argv[2], "w")

for line in infile:
   line_arr = line.split(" ")
   nnz = len(line_arr) - 1
   for i in range(1, len((line_arr))):
       fea_val = float(line_arr[i].split(":")[1])
       if fea_val < 1e-6:
           nnz -= 1
   outfile.write("%d\n" % nnz)
        
