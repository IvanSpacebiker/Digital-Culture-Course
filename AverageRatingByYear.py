import matplotlib.pyplot as plt


class AverageRatingByYear:
    def __init__(self, DATASET, ax):
        years = DATASET["Year"].unique()
        y = [0] * len(years)

        for i in range(len(DATASET)):
            for j in range(len(years)):
                if (DATASET["Year"].loc[i] == years[j]):
                    y[j] += DATASET["Rating"].loc[i]
                    break
        for i in range(len(years)):
            y[i] /= DATASET["Year"].value_counts()[years[i]]

        ax[0, 1].bar(years, y, color = "purple", width = 0.2)
        ax[0, 1].grid()
        ax[0, 1].set_title("Средний рейтинг по годам", fontsize = 10)