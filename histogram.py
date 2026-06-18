import matplotlib.pyplot as plt
import sys
from describe import *
from load_csv import load
import numpy as np

def get_features(df):
    """ignore the non required features"""
    ignore = ["Index", "Hogwarts House", "First Name", "Last Name", "Birthday", "Best Hand"]
    columns = []
    for elem in df.columns:
        if elem in ignore:
            continue
        columns.append(elem)
    return columns

def plot_one(df, feature, ax):
    """show feature"""
    houses = ["Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"]
    colors = {
        "Gryffindor": "red",
        "Ravenclaw": "blue",
        "Hufflepuff": "yellow",
        "Slytherin": "green"
            }
    for house in houses:
        chosen = df[df["Hogwarts House"] == house][feature]
        ax.hist(chosen, label=house, color=colors[house], alpha=0.5, bins=20)
    ax.legend()
    ax.set_title(feature)

def plot_all(df, features):
    """call plot_one for every feature"""
    fig, axes = plt.subplots(3, 5, figsize=(18, 25))
    axes = axes.flatten()
    for i, feature in enumerate(features):
        plot_one(df, feature, axes[i])
    for j in range(len(features), len(axes)):
        axes[j].set_visible(False)
    plt.tight_layout(pad=3.0, h_pad=4.0, w_pad=2.0)
    plt.show()

def histo(dataset: str, subject=None):
    """make a histo"""
    df = emptyfiller(dataset)
    if df is None:
        return
    features = get_features(df)
    if subject is None:
        plot_all(df, features)
    else:
        if subject not in features:
            print("Error: Unknown subject")
            print("Available subjects: ", features)
            return
        fig, ax = plt.subplots()
        plot_one(df, subject, ax)
        plt.show()

def main():
    """entry point of the programm"""
    if len(sys.argv) == 2:
        histo(sys.argv[1])
    elif len(sys.argv) == 3:
        histo(sys.argv[1], sys.argv[2])
    else:
        print("Usage : python3 histogram.py extension.csv [subject]")


if __name__ == "__main__":
    main()



