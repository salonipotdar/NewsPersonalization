import os
import sys
from sets import Set

#count how many user in each cluster, and how many instance in each cluster
#input: clustering_output (step 2 output, contain both user id and cluster id); training_data
clustering_data = open(sys.argv[1])
training_data = open(sys.argv[2])

num_instance_per_cluster = {}
num_user_per_cluster = {}

uid_cluster = {}
for line in clustering_data:
    uid = int(line.split(" ")[0])
    cid = int(line.split(" ")[1])
    uid_cluster[uid] = cid

for line in training_data:
    line = line[:-1]
    line_arr = line.split("|")
    user_id = int(line_arr[1])
    if user_id not in uid_cluster:
        continue
    user_cluster_id = uid_cluster[user_id]
    if user_cluster_id not in num_instance_per_cluster:
        num_instance_per_cluster[user_cluster_id] = 0
    num_instance_per_cluster[user_cluster_id] += 1
    if user_cluster_id in num_user_per_cluster:
        num_user_per_cluster[user_cluster_id].add(user_id)
    else:
        num_user_per_cluster[user_cluster_id] = Set()
        num_user_per_cluster[user_cluster_id].add(user_id)

sorted_num_ins_per_cluster = sorted(num_instance_per_cluster.items())
sorted_num_user_per_cluster = sorted(num_user_per_cluster.items())

num_cluster = len(sorted_num_ins_per_cluster)
for i in range(0, num_cluster):
    if (sorted_num_ins_per_cluster[i][0] != sorted_num_user_per_cluster[i][0]):
        print "error"
        sys.exit(1)
    else:
        print "%d %d %d" % (sorted_num_ins_per_cluster[i][0], sorted_num_ins_per_cluster[i][1], len(sorted_num_user_per_cluster[i][1]))
    
