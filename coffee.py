class Coffee:
    def _init_(self, name):
        # Validate that the name is at least 3 characters long
        if len(name) >= 3:
            self._name = name
        else:
            raise ValueError("Coffee name must be at least 3 characters long")
        
        # Initialize an empty list to hold the orders for this coffee
        self._orders = []

    # Property for getting the coffee's name
    @property
    def name(self):
        return self._name

    # Method to add an order to this coffee's list
    def add_order(self, order):
        # Delay the import to avoid circular dependency
        from order import Order

        if not isinstance(order, Order):
            raise TypeError("order must be an instance of Order")
        self._orders.append(order)

    # Method to return the total number of orders for this coffee
    def num_orders(self):
        return len(self._orders)

    # Method to calculate the average price of the coffee based on orders
    def average_price(self):
        if not self._orders:
            return 0.0
        total_price = sum(order.price for order in self._orders)
        return total_price / len(self._orders)


