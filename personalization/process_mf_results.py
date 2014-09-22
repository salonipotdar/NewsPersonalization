#input user_feature_generated_by_mf, clustering_results, user_id to local_id map, output_file
import os
import sys

user_fea_file = open(sys.argv[1])
cluster_results_file = open(sys.argv[2])
user_localid_map_file = open(sys.argv[3])
output_file = open(sys.argv[4], "w")

localid_to_uid = {}
for line in user_localid_map_file:
    line_arr = line.split(" ")
    localid_to_uid[int(line_arr[1])] = int(line_arr[0])

for line in user_fea_file:
    local_uid = int(line.split(" ")[0])
    global_uid = localid_to_uid[local_uid]
    cluster_id = int(cluster_results_file.readline())
    output_file.write("%d %d\n"%(global_uid, cluster_id))
    
