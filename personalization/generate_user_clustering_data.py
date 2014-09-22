import os
import sys

for line in sys.stdin:
    line_arr = line.split("|")
    user_id = line_arr[1]
    user_feas = line_arr[2].split(" ")
    output_feas = "%s 1:1 %s %s %s %s %s" % (user_id, user_feas[1], user_feas[2], user_feas[3], user_feas[4], user_feas[5])
    print output_feas
