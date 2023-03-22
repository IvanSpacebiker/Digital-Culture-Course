import numpy.random as rand


class PointGenerator:

    def __init__(self, data):
        self.data = data
        self.points = []

    def fit(self):
        pass

    def generate_points(self, n_points):
        for i in range(n_points):
            genre = rand.choice(list(self.data.keys()))
            rating, year = rand.multivariate_normal((self.data[genre].mean_rating, self.data[genre].mean_year), self.data[genre].cov)
            self.points.append([genre, rating, year])

    def log_likelyhood(self, X):
        pass

    def mean_log_likelyhood(self, X):
        pass

    def mean(self, xs):
        return sum(xs) / len(xs)
