import os
import sys

filename = sys.argv[1]
output_filename = sys.argv[2]
f = open(filename)
fout = open(output_filename, "w")
uid = {}
uid_count = {}
cur_id = 1
for line in f:
    line_arr = line.split("|")
    if (line_arr[1] == "user 1 "):
        continue
    user_features = []
    user_features_string = line_arr[1].split(" ")
    for i in range(1, len(user_features_string)):
        if (len(user_features_string[i])) != 0:
            user_features.append(int(user_features_string[i]))
    user_features.sort()
    user_key = str(user_features).strip('[]')
    if user_key in uid:
        uid_count[user_key] = uid_count[user_key] + 1
        fout.write(line_arr[0].strip(' '));
        fout.write("|" + str(uid[user_key]));
        for i in range(2, len(line_arr)):
            fout.write("|" + line_arr[i].strip(' '));
        continue
    uid[user_key] = cur_id
    fout.write(line_arr[0].strip(' '));
    fout.write("|" + str(cur_id));
    for i in range(2, len(line_arr)):
        fout.write("|" + line_arr[i].strip(' '));
    cur_id = cur_id + 1
    uid_count[user_key] = 1
#fout = open(output_filename, "w")
#for key, value in uid.items():
#    fout.write("%d\t%s\n" % (value,key))
#for key, value in uid_count.items():
#    fout.write("%d\t%s\n" % (value, key))
