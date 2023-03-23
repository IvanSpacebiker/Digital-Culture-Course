import matplotlib.pyplot as plt


class PlotDrawer:
    def __init__(self, genres, genre_names, ax):

        # fig = plt.figure(figsize=(8, 8))
        # ax = fig.add_subplot()

        for i in range(len(genres)):
            genre = genres[i].data
            name = genre_names[i]
            ax[0, 0].scatter(genre["Year"], genre["Rating"], label=name)

        ax[0, 0].grid()
        ax[0, 0].legend()

        # plt.tick_params (labelsize = 8)
        # plt.xlabel("Год", fontsize = 10)
        #plt.show()
