# be careful this is column normalization, not row
from sklearn import preprocessing
from sklearn.datasets import load_svmlight_file
from sklearn.datasets import dump_svmlight_file
import numpy as np
import sys
import os

X_train, y_train = load_svmlight_file(sys.argv[1])
X_scaled = preprocessing.scale(X_train.todense())
dump_svmlight_file(X_scaled, y_train, sys.argv[2], zero_based=True)
