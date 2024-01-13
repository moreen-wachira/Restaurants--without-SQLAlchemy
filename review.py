class Review:
    reviews = []

    def __init__(self, customer, restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self._rating = rating
        Review.reviews.append(self)
        customer.reviews.append(self)
        restaurant.reviews.append(self)

    def rating(self):
        return self._rating

    @classmethod
    def all(cls):
        return cls.reviews

    @property
    def customer(self):
        return self._customer

    @property
    def restaurant(self):
        return self._restaurant
