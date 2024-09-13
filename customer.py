from coffee import Coffee  # Import the Coffee class
from order import Order    # Import the Order class

class Customer:
    def _init_(self, name):
        # Validate that the name is between 1 and 15 characters
        if 1 <= len(name) <= 15:
            self._name = name
        else:
            raise ValueError("Customer name must be between 1 and 15 characters")
        
        # Initialize an empty list to hold the orders for this customer
        self._orders = []

    # Property for getting the customer's name
    @property
    def name(self):
        return self._name

    # Method to create an order for this customer
    def create_order(self, coffee, price):
        # Check if the coffee argument is an instance of Coffee class
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be an instance of Coffee")
        if not (1.0 <= price <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0")

        # Create a new order and associate it with the customer and coffee
        order = Order(self, coffee, price)
        self._orders.append(order)
        coffee.add_order(order)
        return order

    # Method to return all orders placed by this customer
    def orders(self):
        return self._orders

        
     
