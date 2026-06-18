import matplotlib.pyplot as plt
import sys
from describe import *
from load_csv import load
import numpy as np
from histogram import *


def find_most_correlated(df, features):
    """return the 2 features the most correlated"""
    corr = []
    for i, feature1 in enumerate(features):
        for j, feature2 in enumerate(features):
            if j <= i:
                continue
            y = df[feature2]
            x = df[feature1]
            res = get_corr(x, y)
            corr.append((abs(res), feature1, feature2)) # abs give absolute
    values = []
    for elem in corr:
        values.append(elem[0])
        max_corr = get_max(*values)
    for elem in corr:
        if elem[0] == max_corr:
            return elem


def plot_scatter(df, feature1, feature2):
        houses = ["Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"]
        colors = {
        "Gryffindor": "red",
        "Ravenclaw": "blue",
        "Hufflepuff": "yellow",
        "Slytherin": "green"
            }
        for house in houses:
            x = df[df["Hogwarts House"] == house][feature1]
            y = df[df["Hogwarts House"] == house][feature2]
            plt.xlabel(feature1)
            plt.ylabel(feature2) 
            plt.scatter(x, y, label=house, color=colors[house])
        plt.legend("feature1 vs feature2")
        plt.show()

def scatter(dataset):
    """call all the previous ft"""
    df = emptyfiller(dataset)
    if df is None:
        return
    features = get_features(df)
    corr = find_most_correlated(df, features)
    plot_scatter(df, corr[1], corr[2])
    

def main():
    """entry point of the programm"""
    if len(sys.argv) != 2:
        print("Usage : python3 scatter_plot.py extension.csv")
        return
    scatter(sys.argv[1])


if __name__ == "__main__":
    main()