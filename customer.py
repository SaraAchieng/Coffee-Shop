from order import Order

class Customer:
    def __init__(self, name):
        # Validate that the name is between 1 and 15 characters
        if 1 <= len(name) <= 15:
            self._name = name
        else:
            raise ValueError("Customer name must be between 1 and 15 characters")
        self.name = name
    # Returns a list of all Order instances associated with this customer
    def orders(self):
        return [order for order in Order.all_orders if order.customer == self]
    
    # Returns a list of unique Coffee instances ordered by this customer
    def coffees(self):
        return list(set([order.coffee for order in self.orders()]))
    
    #Creates a new Order instance for this customer with the given coffee and price
    def create_order(self, coffee, price):
        Order(self, coffee, price)


        
     
