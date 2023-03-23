import matplotlib.pyplot as plt


class NumberOfFilmsOfTheGenre:
    def __init__(self, DATASET, genre_names, ax):
        y = [0] * len(genre_names)

        for i in range(len(genre_names)):
            y[i] = DATASET["Genre"].value_counts()[genre_names[i]]

        ax[1, 0].bar(genre_names, y, width = 0.2)
        ax[1, 0].grid()

        ax[1, 0].set_title("Количество фильмов по жанрам", fontsize = 10)

