from header.load_data_from_csv import *

# Load dataset
filename = "datasets/pima-indians-diabetes.csv"
dataset = load_csv(filename)

print("Loaded data file {0} with {1} rows and {2} columns".format(filename, len(dataset), len(dataset[0])))

# Convert string to float
for i in range(len(dataset[0])):
    str_column_to_float(dataset, i)
print(dataset[0])

# Load dataset
filename = "datasets/iris.csv"
dataset = load_csv(filename)
dataset = dataset[1:] # Remove header
print("Loaded data file {0} with {1} rows and {2} columns".format(filename, len(dataset), len(dataset[0])))

for i in range(4):
    str_column_to_float(dataset, i)

lookup = str_column_to_int(dataset, 4)