from Genre import Genre


class PointGenerator:

    def __init__(self, names):
        self.p = {}
        for name in names:
            self.p.update({name: Genre(name)})

    def fit(self):
        pass

    def generate_points(self):
        pass

    def log_likelyhood(self, X):
        pass

    def mean_log_likelyhood(self, X):
        pass

    def mean(self, xs):
        return sum(xs) / len(xs)
