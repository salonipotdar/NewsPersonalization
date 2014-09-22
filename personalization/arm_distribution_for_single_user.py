import sys
import os

uid = int(sys.argv[1])
datafile = sys.argv[2]
news_pool = {}
f = open(datafile, "r")

for line in f:
   line = line[:-1]
   line_arr = line.split("|")
   if uid != int(line_arr[1]):
      continue
   for i in range(2, len(line_arr)):
      if line_arr[i] not in news_pool:
         news_pool[line_arr[i]] = [1,0,0]
      else:
         news_pool[line_arr[i]][0] += 1
   shown_doc = line_arr[0].split(" ")[1]
   clicked = int(line_arr[0].split(" ")[2])
   news_pool[shown_doc][1] += 1
   if clicked == 1:
      news_pool[shown_doc][2] += 1


for key, value in news_pool.items():
   print "doc %s pool %d shown %d ratio %g click %d ctr %g" % (key, value[0], value[1], float(value[1]) / (value[0]+1), value[2], float(value[2])/(value[1]+1))
