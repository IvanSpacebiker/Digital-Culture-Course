import matplotlib.pyplot as plt


class PlotDrawer:
    def __init__(self, DATASET):

        genreNames = DATASET["Genre"].unique()
        genres = []
        for g in genreNames:
            genres.append(DATASET.where(DATASET["Genre"] == g))

        fig = plt.figure(figsize=(8, 8))
        ax = fig.add_subplot()

        for i in range(len(genres)):
            genre = genres[i]
            name = genreNames[i]
            ax.scatter(genre["Year"], genre["Rating"], label=name)

        ax.grid()
        ax.legend()
        plt.show()
