
        
class Order:
    def __init__(self, customer, coffee, price):
        # Delay the imports
        from customer import Customer
        from coffee import Coffee
        self._customer = customer
        self._coffee = coffee
        self._price = price
        
        if not isinstance(customer, Customer):
            raise TypeError("customer must be an instance of Customer")
        
        # Check if the coffee argument is an instance of Coffee class
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be an instance of Coffee")
        # Validate that the price is between 1.0 and 10.0
        if not (1.0 <= price <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0")
        
        

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
    

        
  
  


