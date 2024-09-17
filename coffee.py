from order import Order

class Coffee:
    def __init__(self, name):
        # Validate that the name is at least 3 characters long
        if len(name) >= 3:
            self._name = name
        else:
            raise ValueError("Coffee name must be at least 3 characters long")
        self.name = name
        
    # Returns a list of all Order instances associated with this coffee
    def orders(self):
        return [order for order in Order.all_orders if order.coffee == self]

    def customers(self):
        return list(set([order.customer for order in self.orders()]))
    
    # Returns the total number of orders for this coffee.
    def num_orders(self):
        return len(self.orders())
    
    # Returns the average price of this coffee based on its orders.
    def average_price(self):
        orders = self.orders()
        if orders:
            total_price = sum(order.price for order in orders)
            return total_price / len(orders)
        return 0


