#python program input_data output_data_with_uid uid_feature_mapping
import os
import sys
import operator

user_fea = {}
uid = 1

finput = open(sys.argv[1])
foutput_data = open(sys.argv[2], "w")
foutput_fea = open(sys.argv[3], "w")

for line in finput:
    line = line[:-1]
    line_arr = line.split("|")
    if line_arr[1] not in user_fea:
        user_fea[line_arr[1]] = uid;
        uid += 1;
    line_arr[1] = str(user_fea[line_arr[1]])
    output_string = "|".join(line_arr)
    foutput_data.write(output_string+"\n")

sorted_user_fea = sorted(user_fea.iteritems(), key=operator.itemgetter(1))
for value in sorted_user_fea:
    value_arr = value[0].split(" ")
    foutput_fea.write("%s 1:1 %s %s %s %s %s\n" % (value[1], value_arr[1], value_arr[2], value_arr[3], value_arr[4], value_arr[5]))
