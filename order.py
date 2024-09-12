from customer import Customer
from coffee import Coffee

# order.py
class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        if not isinstance(value, Customer):
            raise ValueError("Customer must be a valid Customer instance.")
        self._customer = value

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        if not isinstance(value, Coffee):
            raise ValueError("Coffee must be a valid Coffee instance.")
        self._coffee = value
           
