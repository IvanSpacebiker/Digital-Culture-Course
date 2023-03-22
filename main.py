import pandas as pd

from PlotDrawer import PlotDrawer
from PointGenerator import PointGenerator

IMDB_TEST = pd.read_csv("datasets/IMDB-Movie-Data_Test.csv", sep=";")
IMDB_TRAIN = pd.read_csv("datasets/IMDB-Movie-Data_Train.csv", sep=";")

DATASET = IMDB_TEST

genre_names = DATASET["Genre"].unique()
genres = []
for g in genre_names:
    genres.append(DATASET.where(DATASET["Genre"] == g))


graph = PlotDrawer(genres, genre_names)
