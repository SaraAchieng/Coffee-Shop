from customer import Customer
from coffee import Coffee


# Instances of customers 
sara = Customer("Sara")
print(sara.name)
bob = Customer("Bob")
print(bob.name)
ayim = Customer("Ayim")
kim = Customer("Kim")

# Instances of coffee
cof = Coffee("Americano")
print(cof.name)
coffee2 = Coffee("Latte")
coffee3 = Coffee("Black Coffee")
coffee4 = Coffee("Espresso")

# Orders placed by customers
order1 = sara.create_order(cof, 10.0)
order2 = ayim.create_order(cof, 10.0)
order3 = kim.create_order(coffee2, 8.0)
order4 = ayim.create_order(coffee2, 8.0)
order5 = bob.create_order(cof, 10.0)
order6 = ayim.create_order(coffee4, 9.0)
order7 = sara.create_order(coffee3, 5.0)

# Number of orders for each coffee
print(cof.num_orders())  
print(coffee4.num_orders())  
print(coffee3.num_orders()) 


# Average price of coffee
print(cof.average_price())  
print(coffee2.average_price()) 

# List all orders for a customer
for order in sara.orders():
    print(f"Customer: {order.customer.name}, Coffee: {order.coffee.name}, Price: {order.price}")
for order in kim.orders():
    print(f"Customer: {order.customer.name}, Coffee: {order.coffee.name}, Price: {order.price}") 
for order in ayim.orders():
    print(f"Customer: {order.customer.name}, Coffee: {order.coffee.name}, Price: {order.price}")       
    
    
    
    