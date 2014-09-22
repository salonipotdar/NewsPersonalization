#args: input data file, number of cluster, output_file
import os
import sys
from sklearn.datasets import load_svmlight_file
from sklearn.cluster import KMeans
f = open(sys.argv[3], "w")
X_train, y_train = load_svmlight_file(sys.argv[1])
kmean_estimator=KMeans(n_clusters=int(sys.argv[2]), init='k-means++', n_init=10, max_iter=300, tol=0.0001, precompute_distances=True, verbose=0, random_state=None, n_jobs=3)
Y=kmean_estimator.fit_predict(X_train)

for i in Y:
    f.write("%d\n" % i)
