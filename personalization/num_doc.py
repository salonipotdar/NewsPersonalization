import sys
import os
from sets import Set

doc_id = Set()
shown_doc_id = Set()

for line in sys.stdin:
    line = line[:-1]
    line_arr = line.split("|")
    for i in range(2, len(line_arr)):
        doc_id.add(line_arr[i])
    shown_doc = line_arr[0].split(" ")[1]
    shown_doc_id.add(shown_doc)

doc_id_string = ""
for doc in doc_id:
    doc_id_string += doc + " ";

shown_doc_id_string = ""
for doc in shown_doc_id:
    shown_doc_id_string += doc + " ";

print doc_id_string
print shown_doc_id_string
