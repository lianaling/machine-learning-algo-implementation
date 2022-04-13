from header.scale_machine_learning_data import *
from header.load_data_from_csv import load_csv, str_column_to_float

filename = "datasets/pima-indians-diabetes.csv"
norm_dataset = load_csv(filename)
for i in range(len(norm_dataset[0])):
    str_column_to_float(norm_dataset, i)

# Normalise dataset
minmax = dataset_minmax(norm_dataset)
normalize_dataset(norm_dataset, minmax)
print(norm_dataset[0])

# Mock dataset
# dataset = [[50, 30], [20, 90], [30, 50]]
# print(dataset)

# means = column_means(dataset)
# stdevs = column_stdevs(dataset, means)
# print("means: ", means)
# print("stdevs", stdevs)

# standardize_dataset(dataset, means, stdevs)
# print(dataset)
stan_dataset = load_csv(filename)
for i in range(len(stan_dataset[0])):
    str_column_to_float(stan_dataset, i)

means = column_means(stan_dataset)
stdevs = column_stdevs(stan_dataset, means)
standardize_dataset(stan_dataset, means, stdevs)
print(stan_dataset[0])