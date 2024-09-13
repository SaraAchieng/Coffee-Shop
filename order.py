class Order:
    def _init_(self, customer, coffee, price):
        # Delay the imports to avoid circular dependency
        from customer import Customer
        from coffee import Coffee
        
        # Check if the customer argument is an instance of Customer class
        if not isinstance(customer, Customer):
            raise TypeError("customer must be an instance of Customer")
        # Check if the coffee argument is an instance of Coffee class
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be an instance of Coffee")
        # Validate that the price is between 1.0 and 10.0
        if not (1.0 <= price <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0")

        # Associate this order with the customer, coffee, and price
        self._customer = customer
        self._coffee = coffee
        self._price = price

    # Properties for customer, coffee, and price
    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price
    

        
  
  


