import numpy as np
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split

def read_from_file(filename):
    file_handler = open(filename, "r")
    raw_data = []
    for line in file_handler:
        raw_data.append(line.strip('\n'))
    file_handler.close()
    # Remove first row of column header
    raw_data = raw_data[1:]
    return raw_data

def wine_quality_helper(raw_data):
    # Split each line on ';'
    wine_list = []

    for line in raw_data:
        arr = [float(i) for i in line.split(';')]
        wine_list.append(arr)

    return wine_list

def wine_type_helper(raw_data, label):
    # remove quality labels, add classfication labels for red/white
    wine_list = []

    for line in raw_data:
        arr = [float(i) for i in line.split(';')]
        arr = arr[:-1] + [label]
        wine_list.append(arr)

    return wine_list

def prepare_wine_quality_data():
    w_raw = read_from_file("./winequality-white.csv")
    r_raw = read_from_file("./winequality-red.csv")

    full_wines_list = wine_quality_helper(w_raw) + wine_quality_helper(r_raw)
    full_wines_list = np.array(full_wines_list)
    print full_wines_list.shape
    # Data is features in the first 11 columns, Labels are the values in last column
    data = full_wines_list[:, :-1]
    labels = full_wines_list[:, 11]
    print data
    print labels

    return train_test_split(data, labels, test_size=0.2, random_state=42)

def prepare_wine_type_data():
    # Red wine label 1
    # White wine label 0
    w_raw = read_from_file("./winequality-white.csv")
    r_raw = read_from_file("./winequality-red.csv")

    full_wines_list = wine_type_helper(w_raw, 0) + wine_type_helper(r_raw, 1)
    full_wines_list = np.array(full_wines_list)
    print full_wines_list.shape
    # Data is features in the first 11 columns, Labels are the values in last column
    data = full_wines_list[:, :-1]
    labels = full_wines_list[:, 11]
    print data
    print labels

    return train_test_split(data, labels, test_size=0.2, random_state=42)
