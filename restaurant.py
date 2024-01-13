class Restaurant:
    restaurants = []

    def __init__(self, name):
        self._name = name
        self.reviews = []
        Restaurant.restaurants.append(self)

    def name(self):
        return self._name

    @classmethod
    def all(cls):
        return cls.restaurants

    def reviews(self):
        return self.reviews

    def customers(self):
        return list(set([review.customer for review in self.reviews]))

    def average_star_rating(self):
        if not self.reviews:
            return 0
        return sum([review.rating() for review in self.reviews]) / len(self.reviews)
