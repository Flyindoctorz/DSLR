from histogram import *
import matplotlib.pyplot as plt
import sys
from describe import *
from load_csv import load
import numpy as np

def plot_pair(df, feature_x, feature_y, ax):
	"""draw the scatter on the ax"""
        houses = ["Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"]
        colors = {
        "Gryffindor": "red",
        "Ravenclaw": "blue",
        "Hufflepuff": "yellow",
        "Slytherin": "green"
            }
        for house in houses:
            x = df[df["Hogwarts House"] == house][featurex]
            y = df[df["Hogwarts House"] == house][featurey]
            ax.scatter(x, y, label=house, color=colors[house])

def pair_plot(df, features):
	"""call pair plot when i != j and plot_one when i == j"""
	N = 0
	for f in features:
		N += 1
	fig, axes = plt.subplots(N, N, figsize=(18, 25))
    axes = axes.flatten()
		for i, feature_y in enumerate(features):
			for j, feature_x in enumerate(features):
				index = i * N + j
				if i == j:
					plot_one(df, feature_y, axes[index])
				else:
					plot_pair(df, feature_x, feature_y, axes[index])
				if i == N - 1:
					axes[index].set_xlabel(feature_x)
				if j == 0:
					axes[index].set_ylabel(feature_y)
	plt.show()
		 
		



