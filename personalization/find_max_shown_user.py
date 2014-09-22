import sys
import os
from operator import itemgetter

user_count = {}

for line in sys.stdin:
    line_arr = line.split("|")
    uid = int(line_arr[1])
    if uid in user_count:
        user_count[uid] = user_count[uid] + 1
    else:
        user_count[uid] = 1


sorted_user_id = sorted(user_count.items(), key=itemgetter(1), reverse=True)

for i in range(0, 10):
	print "%d %d " % (sorted_user_id[i][0], sorted_user_id[i][1])
