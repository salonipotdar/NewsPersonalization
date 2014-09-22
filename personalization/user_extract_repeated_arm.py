import os
import sys

filename = sys.argv[1]
output_filename = sys.argv[2]
fout = open(output_filename, "w")
f = open(filename)
uid = {}
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

    info_arr = line_arr[0].split(" ")
    click = int(info_arr[2])
    if user_key in uid:
        this_uid = uid[user_key]
        fout.write("%d\t%s\t%d\n" % (this_uid, info_arr[1], click))
        continue
    uid[user_key] = cur_id
    fout.write("%d\t%s\t%d\n" % (cur_id, info_arr[1], click))
    cur_id = cur_id + 1
