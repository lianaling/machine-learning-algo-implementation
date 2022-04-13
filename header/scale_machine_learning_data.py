# Normalisation is rescaling between 0 and 1. Requires max and min values.

from math import sqrt


def dataset_minmax(dataset: list[list]) -> list[int]:
    minmax = list()
    for i in range(len(dataset[0])):
        col_values = [row[i] for row in dataset]
        value_min = min(col_values)
        value_max = max(col_values)
        minmax.append([value_min, value_max])
    return minmax

def normalize_dataset(dataset: list[list], minmax: list) -> None:
    for row in dataset:
        for i in range(len(row)):
            row[i] = (row[i] - minmax[i][0]) / (minmax[i][1] - minmax[i][0])

# Standardisation is centering the data distribution on the value 0 and the standard deviation to the value 1. The mean and standard deviation can be used to summarise a normal distribution known as Gaussian distribution. Requires the mean and standard deviation.

def column_means(dataset: list[list]) -> list[float]:
    # Init mean with 0
    means = [0 for _ in range(len(dataset[0]))]
    for i in range(len(dataset[0])):
        col_values = [row[i] for row in dataset]
        means[i] = sum(col_values) / float(len(dataset))
    return means

def column_stdevs(dataset: list[list], means: list[float]) -> list[float]:
    # sum_of_squared_diff = [0 for _ in range(len(dataset[0]))]
    stdevs = [0 for _ in range(len(dataset[0]))]
    for i in range(len(dataset[0])):
        squared_diff = [pow(row[i] - means[i], 2) for row in dataset]
        stdevs[i] = sum(squared_diff)
    stdevs = [sqrt(x / float((len(dataset) - 1))) for x in stdevs]
    return stdevs

def standardize_dataset(dataset: list[list], means: list[float], stdevs: list[float]) -> None:
    for row in dataset:
        for i in range(len(row)):
            row[i] = (row[i] - means[i]) / stdevs[i]

# Use standardisation when the data follows a normal distribution. Normalisation does not assume any specific distribution.