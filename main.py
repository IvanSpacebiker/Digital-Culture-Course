import pandas as pd

from PlotDrawer import PlotDrawer

IMDB_TEST = pd.read_csv("datasets/IMDB-Movie-Data_Test.csv", sep=";")
IMDB_TRAIN = pd.read_csv("datasets/IMDB-Movie-Data_Train.csv", sep=";")

graph = PlotDrawer(IMDB_TEST)
