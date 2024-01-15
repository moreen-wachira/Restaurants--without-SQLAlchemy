# review.py
class Review:
    reviews = []

    def __init__(self, customer, restaurant, stars):
        self.customer = customer
        self.restaurant = restaurant
        self.stars = stars
        Review.reviews.append(self)
        customer.reviews.append(self)
        restaurant.reviews.append(self)

    @classmethod
    def all(cls):
        return cls.reviews