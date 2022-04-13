from header.algo_eval_methods import *
from header.scale_machine_learning_data import column_means, column_stdevs

from random import seed

# Split into train and test datasets
seed(1)
dataset = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
train, test = train_test_split(dataset)
print("train: ", train)
print("test: ", test)

# Split using k-fold cross validation
seed(1)
folds = cross_validation_split(dataset, 4)
print("folds: ", folds)

# Validate if folds are sufficiently representative
mean = column_means(dataset)
stdev = column_stdevs(dataset, mean)
print("[DATASET]\nmeans: {}\nstdevs: {}".format(mean, stdev))

for i in range(len(folds)):
    mean = column_means(folds[i])
    stdev = column_stdevs(folds[i], mean)
    print("[FOLD {}]\nmeans: {}\nstdevs: {}".format(i, mean, stdev))