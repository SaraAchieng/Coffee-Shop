# customer.py
class Customer:
    _orders = []

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        if not (1 <= len(value) <= 15):
            raise ValueError("Name must be between 1 and 15 characters.")
        self._name = value

    def orders(self):
        """Return a list of all orders for this customer."""
        return [order for order in Customer._orders if order.customer == self]

    def coffees(self):
        """Return a unique list of coffees that this customer has ordered."""
        return list(set(order.coffee for order in self.orders()))

    @classmethod
    def add_order(cls, order):
        """Register a new order for the customer."""
        cls._orders.append(order)

    