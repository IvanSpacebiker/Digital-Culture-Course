import matplotlib.pyplot as plt


class PlotDrawer:
    def __init__(self, genres, genre_names):

        fig = plt.figure(figsize=(8, 8))
        ax = fig.add_subplot()

        for i in range(len(genres)):
            genre = genres[i]
            name = genre_names[i]
            ax.scatter(genre["Year"], genre["Rating"], label=name)

        ax.grid()
        ax.legend()
        plt.show()
