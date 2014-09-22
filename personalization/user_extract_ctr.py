import os
import sys

filename = sys.argv[1]
output_filename = sys.argv[2]
f = open(filename)
uid = {}
uid_show = {}
uid_click = {}
total_show = 0
total_click = 0
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
        uid_show[this_uid] = uid_show[this_uid] + 1
        if click == 1:
            uid_click[this_uid] = uid_click[this_uid] + 1
        continue
    uid[user_key] = cur_id
    uid_show[cur_id] = 1;
    if click == 1:
        uid_click[cur_id] = 1;
    else:
        uid_click[cur_id] = 0;
    cur_id = cur_id + 1
fout = open(output_filename, "w")
#for key, value in uid.items():
#    fout.write("%d\t%s\n" % (value,key))
for key, value in uid.items():
    fout.write("%d\t%d\t%g\t%s\n" % (uid_show[value], uid_click[value], uid_click[value] / float(uid_show[value]), key))
