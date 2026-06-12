from load_csv import load
import numpy as np
import pandas as pd
from useful import get_mean, get_var, get_std


def emptyfiller(dataset: str):
    """fills the empty fields by the median of the column"""
    df = load(dataset)
    house = df["Hogwarts House"]
    ignore = ["Index", "Hogwarts House", "First Name", "Last Name", "Birthday", "Best Hand"]
    for column in df.columns:
        if column in ignore:
            continue
        count = 0
        values = []
        for value in df[column]:
            if value == value: #skip empty rows
                count+= 1
                values.append(value)
        values.sort()
        if count  % 2 == 0:
            median = (values[count // 2 + 1] + values[count // 2]) / 2
        else:
            median = values[count // 2]
        for i, value in enumerate(df[column]):
            if value != value:
                df.at[i, column] = median
    return df.to_csv("dataset_filled.csv", index=False)


def normalizer(dataset: str):
    """normalize the datas inside"""
    df = load(dataset)
    ignore = ["Index", "Hogwarts House", "First Name", "Last Name", "Birthday", "Best Hand"]
    for column in df.columns:
        if column in ignore:
            continue
        mean = get_mean(*df[column])
        std = get_std(*df[column])
        for i, value in enumerate(df[column]):
            df.at[i, column] = (value - mean) / std
        return df.to_csv("dataset_normalised", index=False)

def describe(dataset: str):
    """takes a dataset and return some stats"""
    df = load(dataset)
    ignore = ["Index", "Hogwarts House", "First Name", "Last Name", "Birthday", "Best Hand"]
    columns = []
    means = []
    stds = []
    mins = []
    q1s = []
    q2s = []
    q3s = []
    maxs = []
    for column in df.columns:
        if column in ignore:
            continue
        columns.append(column)
        mean.append(get_mean(*df[column]))
        std.append(get_std(*df[column]))
        mins.append(get_min(*df[column]))
        q1s.append(get_q1(*df[column]))
        q2.append(get_q2(*df[column]))
        q3.append(get_q3(*df[column]))
        maxs.append(get_max(*df[column]))
    print(f"{'':10}", end="")
    for col in columns:
        print(f"{col:15}", end="")
    print()
    print(f"{'Mean':10}", end="")
    for mean in means:
        print(f"{mean:<15.6f}", end="")
    print()


        


    
def main():
    """entry point of the programm"""
    emptyfiller("dataset_train.csv")
    normalizer("dataset_filled.csv")



if __name__ == "__main__":
    main()