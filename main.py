import pandas as pd
from matplotlib import pyplot as plt

from PlotDrawer import PlotDrawer
from PointGenerator import PointGenerator
from Genre import Genre

IMDB_TEST = pd.read_csv("datasets/IMDB-Movie-Data_Test.csv", sep=";")
IMDB_TRAIN = pd.read_csv("datasets/IMDB-Movie-Data_Train.csv", sep=";")

DATASET = IMDB_TRAIN

genre_names = DATASET["Genre"].unique()

genre_duplet = {}
for g in genre_names:
    genre_duplet.update({g: Genre(g, DATASET)})

# Point Generator

# gen = PointGenerator(genre_duplet)
# gen.generate_points(100)
#
# fig = plt.figure(figsize=(8, 8))
# ax = fig.add_subplot()
#
# for i in range(100):
#     ax.scatter(gen.points[i][2], gen.points[i][1])
#
# ax.grid()
# ax.legend()
# plt.show()

genres = list(genre_duplet.values())

graph = PlotDrawer(genres, genre_names)
