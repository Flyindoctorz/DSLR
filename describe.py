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


    
def main():
    """entry point of the programm"""
    emptyfiller("dataset_train.csv")
    normalizer("dataset_filled.csv")



if __name__ == "__main__":
    main()