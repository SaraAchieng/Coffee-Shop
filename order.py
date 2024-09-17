class Order:
    # Class variable to keep track of all Order instances
    all_orders = []

    def __init__(self, customer, coffee, price):
        
         # Delay the imports
        from customer import Customer
        from coffee import Coffee
      
        self.customer = customer
        self.coffee = coffee
        self.price = price
        # Add the new order to the list of all orders
        Order.all_orders.append(self)
        
        # Validate the customer parameter
        if not isinstance(customer, Customer):
            raise ValueError("customer must be an instance of Customer")
        
        # Check if the coffee argument is an instance of Coffee class
        if not isinstance(coffee, Coffee):
            raise ValueError("coffee must be an instance of Coffee")
        # Validate that the price is between 1.0 and 10.0
        if not (1.0 <= price <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0")
        
    #Returns the Customer instance associated with this order.
    @property
    def customer(self):
        return self._customer
    # Sets the Customer instance for this order
    @customer.setter
    def customer(self, customer):
        self._customer = customer
        
    #Returns the Coffee instance associated with this order.
    @property
    def coffee(self):
        return self._coffee
    # Sets the Coffee instance for this order
    @coffee.setter
    def coffee(self, coffee):
        self._coffee = coffee

    

        
  
  


