# restaurant.py
class Restaurant:
    restaurants = []

    def __init__(self, name):
        self.name = name
        self.reviews = []
        Restaurant.restaurants.append(self)

    @classmethod
    def all(cls):
        return cls.restaurants

    def customers(self):
        return [review.customer for review in self.reviews]

    def average_star_rating(self):
        if not self.reviews:
            return 0
        total_rating = sum(review.stars for review in self.reviews)
        return total_rating / len(self.reviews)