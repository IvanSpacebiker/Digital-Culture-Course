import pandas as pd
from matplotlib import pyplot as plt

from PlotDrawer import PlotDrawer
from PointGenerator import PointGenerator
from Genre import Genre
from NumberOfFilmsOfTheGenre import NumberOfFilmsOfTheGenre
from AverageRatingByGenre import AverageRatingByGenre
from AverageRatingByYear import AverageRatingByYear

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
fig = plt.figure(constrained_layout=True, figsize=(18, 8))
ax = fig.subplots(2, 2)
#figure, ax = plt.subplots(2, 2, figsize = (13, 13))
#figure.set_size_inches(10, 10, forward=True)
genres = list(genre_duplet.values())
graph_train = PlotDrawer(genres, genre_names, ax)

genres_number_histogram = NumberOfFilmsOfTheGenre(DATASET, genre_names, ax)
average_rating_by_genre_histogram = AverageRatingByGenre(DATASET, genre_names, ax)
average_rating_by_year_histogram = AverageRatingByYear(DATASET, ax)

ax[0, 0].tick_params(labelsize=8)
ax[1, 0].tick_params(labelsize=8)
ax[0, 1].tick_params(labelsize=8)
ax[1, 1].tick_params(labelsize=8)
# manager = plt.get_current_fig_manager()
# manager.full_screen_toggle()
plt.show()