# customer.py
class Customer:
    customers = []

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.reviews = []
        Customer.customers.append(self)

    @classmethod
    def all(cls):
        return cls.customers

    def restaurants(self):
        return [review.restaurant for review in self.reviews]