import os
import sys

f = open(sys.argv[1])
fout = open(sys.argv[2], "w")

for line in f:
    line_arr = line.split(" ")
    output_string = ""
    for i in range(1, len(line_arr)):
        value = line_arr[i].split(":")
	if len(value) != 2:
            print line
        if i == 1:
            output_string += value[1]
        else:
            output_string += " " + value[1]
    fout.write("%s" % output_string)
        
