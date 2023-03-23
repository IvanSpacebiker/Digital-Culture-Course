import matplotlib.pyplot as plt


class AverageRatingByGenre:
    def __init__(self, DATASET, genre_names, ax):
        y = [0] * len(genre_names)

        for i in range(len(DATASET)):
            for j in range(len(genre_names)):
                if (DATASET["Genre"].loc[i] == genre_names[j]):
                    y[j] += DATASET["Rating"].loc[i]
                    break
        for i in range(len(genre_names)):
            y[i] /= DATASET["Genre"].value_counts()[genre_names[i]]

        ax[1, 1].bar(genre_names, y, color = "firebrick", width = 0.2)
        ax[1, 1].grid()
        ax[1, 1].set_title("Средний рейтинг по жанрам", fontsize = 10)
