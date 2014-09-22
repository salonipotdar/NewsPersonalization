#get the number of times a user shown in the data
import sys
import os

f = open(sys.argv[1])
fout = open(sys.argv[2], "w")
user_count = {}

for line in f:
    line_arr = line.split("|")
    uid = int(line_arr[1])
    if uid not in user_count:
        user_count[uid] = 0
    user_count[uid] += 1

users = sorted(user_count.items())

# 0 1 5 10 100 500 1000 5000 10000
hist = [0,0,0,0,0,0,0,0,0]
hist2 = [0,0,0,0,0,0,0,0,0]
for value in users:
    hist[0] += 1
    hist2[0] += value[1]
    if value[1] > 1:
        hist[1] += 1
        hist2[1] += value[1]
    if value[1] > 5:
        hist[2] += 1
        hist2[2] += value[1]
    if value[1] > 10:
        hist[3] += 1
        hist2[3] += value[1]
    if value[1] > 100:
        hist[4] += 1
        hist2[4] += value[1]
    if value[1] > 500:
        hist[5] += 1
        hist2[5] += value[1]
    if value[1] > 1000:
        hist[6] += 1
        hist2[6] += value[1]
    if value[1] > 5000:
        hist[7] += 1
        hist2[7] += value[1]
    if value[1] > 10000:
        hist[8] += 1
        hist2[8] += value[1]
for value in users:
    fout.write("%d %d\n" % (value[0], value[1]))    
print hist
print hist2
