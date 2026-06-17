from load_csv import load
import numpy as np
import pandas as pd
from useful import *
import sys


def emptyfiller(dataset: str):
    """fills the empty fields by the median of the column"""
    df = load(dataset)
    if df is None:
        return None
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
    # return df.to_csv("dataset_filled.csv", index=False)
    return (df)



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
        return df.to_csv("dataset_normalised.csv", index=False)


def describe(dataset: str):
    """takes a dataset and return some stats"""
    df = emptyfiller(dataset)
    if df is None:
        return
    ignore = ["Index", "Hogwarts House", "First Name", "Last Name", "Birthday", "Best Hand"]
    columns = []
    means = []
    stds = []
    mins = []
    q1s = []
    q2s = []
    q3s = []
    maxs = []
    counts = []
    for column in df.columns:
        if column in ignore:
            continue
        count = 0
        for value in df[column]:
            if value == value:
                count += 1
        counts.append(count)
        columns.append(column)
        means.append(get_mean(*df[column]))
        stds.append(get_std(*df[column]))
        mins.append(get_min(*df[column]))
        q1s.append(get_q1(*df[column]))
        q2s.append(get_q2(*df[column]))
        q3s.append(get_q3(*df[column]))
        maxs.append(get_max(*df[column]))
    print(f"{'':15}", end="")
    for col in columns:
        print(f"{col:15}", end="")
    print()
    print(f"{'Count':15}", end="")
    for val in counts:
        print(f"{val:<15.6f}", end="")
    print()
    print(f"{'Mean':15}", end="")
    for val in means:
        print(f"{val:<15.6f}", end="")
    print()
    print(f"{'Std':15}", end="")
    for val in stds:
        print(f"{val:<15.6f}", end="")
    print()
    print(f"{'Min':15}", end="")
    for val in mins:
        print(f"{val:<15.6f}", end="")
    print()
    print(f"{'25%':15}", end="")
    for val in q1s:
        print(f"{val:<15.6f}", end="")
    print()
    print(f"{'50%':15}", end="")
    for val in q2s:
        print(f"{val:<15.6f}", end="")
    print()
    print(f"{'75%':15}", end="")
    for val in q3s:
        print(f"{val:<15.6f}", end="")
    print()
    print(f"{'Max':15}", end="")
    for val in maxs:
        print(f"{val:<15.6f}", end="")
    print()



    
def main():
    """entry point of the programm"""
    if len(sys.argv) != 2:
        print("Usage: python3 describe.py [extension.csv]")
        return
    #normalizer("dataset_filled.csv")
    describe(sys.argv[1])




if __name__ == "__main__":
    main()