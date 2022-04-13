from random import randrange
from typing import Tuple

def train_test_split(dataset: list[list], split=0.60) -> "Tuple[list[list], list[list]]":
    '''Most widely used as it is easy and quick. Limitation: a noisy estimate of algo performance (less of a problem if it is a very large dataset, e.g. hundred thousands/millions records).'''
    train = list()
    train_size = split * len(dataset)
    dataset_copy = dataset[:]
    while len(train) < train_size:
        index = randrange(len(dataset_copy))
        train.append(dataset_copy.pop(index))
    return train, dataset_copy

def cross_validation_split(dataset: list[list], folds=3) -> "list[list[list]]":
    '''Gold standard. Highly reccommended over `train_test_split`. Default 3 folds (recommended for smaller data). Recommended 10 folds for larger data. Groups should be representative (mean and standard deviation should not differ too much for each fold).'''
    dataset_split = []
    dataset_copy = dataset[:]
    fold_size = int(len(dataset) / folds)
    for _ in range(folds):
        fold = []
        while len(fold) < fold_size:
            index = randrange(len(dataset_copy))
            fold.append(dataset_copy.pop(index))
        dataset_split.append(fold)
    return dataset_split