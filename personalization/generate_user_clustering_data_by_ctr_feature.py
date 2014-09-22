import os
import sys
from sets import Set

user_freq_threshold = int(sys.argv[1])
user_freq_file = sys.argv[2]
ctr_data_file = sys.argv[3]
output_file = sys.argv[4]

users = Set()
fuser_freq = open(user_freq_file)
fctr_data = open(ctr_data_file)
fout = open(output_file, "w")

for line in fuser_freq:
    line_arr = line.split(" ")
    uid = int(line_arr[0])
    freq = int(line_arr[1])
    if freq < user_freq_threshold:
        continue
    users.add(uid)


for line in fctr_data:
    line_arr = line.split(" ")
    uid = int(line_arr[0])
    if uid not in users:
        continue
    fout.write(line)
