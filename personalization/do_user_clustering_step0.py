#args: input data file, number of reduced dim, output_file
import os
import sys
from sklearn.datasets import load_svmlight_file
from sklearn.decomposition import PCA

f = open(sys.argv[3], "w")
X_train, y_train = load_svmlight_file(sys.argv[1])
pca=PCA(n_components=int(sys.argv[2]), copy=False, whiten=False)
X_new = pca.fit_transform(X_train.todense())

#print X_new
ins_id = 0
for ins in X_new:
    output_string = "%d" % y_train[ins_id]
    fea_id = 1
    for fea in ins:
        output_string += " %d:%g" % (fea_id, fea)
        fea_id += 1
    ins_id += 1
    f.write("%s\n" % output_string)
