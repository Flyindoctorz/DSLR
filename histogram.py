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

def plot_one(df, feature, ax)
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
	fig, axes = plt.subplots(5, 3, figsize=(15, 20))
	axes = axes.flatten()
	for i, features in enumerate(features):
		plot_one(df, feature, axes[i])
	for j in range(len(features), len(axes)):
		axes[j].set_visible(False)
	plt.tight_layout()
	plt_show()
		


def histo(dataset: str)
	"""make a histo"""
	df = emptyfiller(dataset)
    if df is None:
        return

def main():
	"""entry point of the programm"""

