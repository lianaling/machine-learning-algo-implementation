from csv import reader

def load_csv(filename: str) -> list:
    '''Load a CSV file that skips empty lines'''
    dataset = list()
    with open(filename, "r") as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)

    __print_loaded_dataset(filename, dataset)
    return dataset

def __print_loaded_dataset(filename: str, dataset: list[list]) -> None:
    print("Loaded data file {0} with {1} rows and {2} columns".format(filename, len(dataset), len(dataset[0])))

def str_column_to_float(dataset: list[list], column: int) -> None:
    '''Convert string column to float'''
    for row in dataset:
        row[column] = float(row[column].strip())

def str_column_to_int(dataset: list[list], column: int) -> 'dict[str, int]':
    '''Convert string to int'''
    # Locate all unique classes
    class_values = [row[column] for row in dataset]
    unique = set(class_values)
    lookup = dict()

    # Store the dict for string and int values
    for i, value in enumerate(unique):
        lookup[value] = i

    # Assign random integer values to the classes
    for row in dataset:
        row[column] = lookup[row[column]]
    return lookup