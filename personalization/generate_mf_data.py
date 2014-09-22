# generate matrix factorization data
# user_id doc_id ctr
# user_id is mapped to local id start from 0, so are doc_id
# output:
# mf training data; user_id_map, doc_id_map
# python program input_training_data user_freq_file user_freq_threshold output_training_data user_id_map_file doc_id_map_file do_normalize

import os
import sys
from sets import Set
import numpy

fdata = open(sys.argv[1])
fuser_freq = open(sys.argv[2])
user_freq_threshold = int(sys.argv[3])
fout_data = open(sys.argv[4], "w")
fout_uidmap = open(sys.argv[5], "w")
fout_didmap = open(sys.argv[6], "w")
#do_normalize = bool(sys.argv[7])

user_freq = {}
for line in fuser_freq:
    uid = int(line.split(" ")[0])
    freq = int(line.split(" ")[1])
    user_freq[uid] = freq

doc_set = Set()

user_ctr = {}
user_localid = {}
doc_localid = {}
local_uid = 0
local_did = 0
for line in fdata:
    line = line[:-1]
    line_arr = line.split("|")
    user_id = int(line_arr[1])
    if user_freq[user_id] < user_freq_threshold:
        continue
    if user_id not in user_localid:
        user_localid[user_id] = local_uid
        local_uid += 1
    shown_doc = int(line_arr[0].split(" ")[1])
    if shown_doc not in doc_localid:
        doc_localid[shown_doc] = local_did
        local_did += 1
    clicked = int(line_arr[0].split(" ")[2])
    doc_set.add(shown_doc)

    if user_id not in user_ctr:
        user_ctr[user_id] = {}
    if shown_doc not in user_ctr[user_id]:
        user_ctr[user_id][shown_doc] = [0,0]
    user_ctr[user_id][shown_doc][0] += 1
    if clicked == 1:
        user_ctr[user_id][shown_doc][1] += 1

for uid, value in user_ctr.items():
    ctr_sum = 0.0
    for doc, data in value.items():
        #if data[0] < 3:
        #    continue
        ctr = float(data[1])/data[0]
        ctr_sum += ctr
    for doc, data in value.items():
        #if data[0] < 3:
        #    continue
        ctr = float(data[1])/data[0]
        if ctr_sum == 0:
            fout_data.write("%d %d %g\n" % (user_localid[uid], doc_localid[doc], 0))
        else:
            fout_data.write("%d %d %g\n" % (user_localid[uid], doc_localid[doc], ctr/ctr_sum))

for key,value in user_localid.items():
    fout_uidmap.write("%d %d\n" % (key, value))
for key,value in doc_localid.items():
    fout_didmap.write("%d %d\n" % (key, value))
