from customer import Customer
from restaurant import Restaurant
from review import Review

# Create instances
customer1 = Customer("John", "Doe")
customer2 = Customer("Jane", "Smith")

restaurant1 = Restaurant("The Taste Place")
restaurant2 = Restaurant("Food Haven")

# Add reviews
review1 = Review(customer1, restaurant1, 4)
review2 = Review(customer2, restaurant1, 5)
review3 = Review(customer1, restaurant2, 3)

# Test methods
print("All customers:", Customer.all())
print("All restaurants:", Restaurant.all())
print("All reviews:", Review.all())

# Test relationships
print("Customer 1's restaurants:", customer1.restaurants())
print("Restaurant 1's customers:", restaurant1.customers())
print("Average rating for Restaurant 1:", restaurant1.average_star_rating())
