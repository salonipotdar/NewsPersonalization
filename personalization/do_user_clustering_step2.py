#the second step is to merge the cluster results with the user id

import os
import sys

fcluster_results = open(sys.argv[1])
fcluster_training_data =open(sys.argv[2])
fout = open(sys.argv[3], "w")

cluster_res = []
for line in fcluster_results:
    cluster_res.append(int(line))
    
uid_list = []
for line in fcluster_training_data:
    uid_list.append(int(line.split(" ")[0]))

assert len(uid_list) == len(cluster_res)

for i in range(0, len(uid_list)):
    fout.write("%d %d\n" % (uid_list[i], cluster_res[i]))
