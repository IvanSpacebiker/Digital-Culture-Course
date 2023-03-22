class Genre:
    def __init__(self, name, DATASET):
        self.name = name
        self.data = DATASET.where(DATASET["Genre"] == name)
        self.p = self.data.count()["Genre"] / len(self.data)
        mean = self.data.mean(0, numeric_only=True)
        self.mean_rating = mean["Rating"]
        self.mean_year = mean["Year"]
        self.cov = self.data.cov(numeric_only=True)

