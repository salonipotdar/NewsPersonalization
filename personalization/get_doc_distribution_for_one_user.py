import os
import sys

uid = int(sys.argv[1])
f = open(sys.argv[2])

doc_count = {}

for line in f:
    line_arr = line.split("|")
    user_id = int(line_arr[1])
    if uid != user_id:
        continue
    doc_id = line_arr[0].split(" ")[1]
    if doc_id not in doc_count:
        doc_count[doc_id] = 0
    doc_count[doc_id] += 1

sorted_doc_count = sorted(doc_count.items())

for value in sorted_doc_count:
    print "%s %s" % (value[0], value[1])
