import matplotlib.pyplot as plt
import sys
from describe import *
from load_csv import load
import numpy as np

def histo_stats(dataset: str, feature: str, stat: str):
    """make a histogram from stats"""
    df = emptyfiller(dataset)
    if df is None:
        return
    houses = ["Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"]
    res = []
    for house in houses:
        chosen = df[df["Hogwarts House"] == house][feature]
        if stat == "mean":
            res.append(get_mean(*chosen))
        elif stat == "std":
            res.append(get_std(*chosen))
        elif stat == "min":
            res.append(get_min(*chosen))
        elif stat == "max":
            res.append(get_max(*chosen))
        elif stat == "q1":
            res.append(get_q1(*chosen))
        elif stat == "q2":
            res.append(get_q2(*chosen))
        elif stat == "q3":
            res.append(get_q3(*chosen))
    plt.figure(figsize=(10, 6))
    plt.ylabel(feature)
    plt.bar(houses, res)
    plt.title(f"{stat} of {feature} by house")
    plt.show()


def main():
    """entry point of the programm"""
    if len(sys.argv) != 4:
        print("Usage: python3 visualize.py [extension.csv] feature stats")
        return
    histo_stats(sys.argv[1], sys.argv[2], sys.argv[3])


if __name__ == "__main__":
    main()

