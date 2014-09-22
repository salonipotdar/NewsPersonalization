import sys
import os

f=open(sys.argv[1])
fout = open(sys.argv[2], "w")
d = {}
for line in f:
	line = line.split("\t")
	if line[0] in d:
		d[line[0]] = d[line[0]] + 1
	else:
		d[line[0]] = 1

f.close();

f=open(sys.argv[1])

for line in f:
	line_arr = line.split("\t")
	if (d[line_arr[0]] == 1):
		continue
	else:
		fout.write("%d\t%s"%(d[line_arr[0]], line))
			
