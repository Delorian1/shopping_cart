from product import Product
from customer import Customer

# As a developer, I want to import the Customer and Product classes into main.py so I can instantiate a customer object as well as three Product objects and interact with the object’s methods:

# 1. Print the customer’s name to the terminal

# 2. Call the customer’s add product to shopping cart 
# method three times and add the three products objects you created

# 3. Call the customer’s view products method

# 4. Call the customer’s shopping cart’s get cart total method. 
# Capture the total the method returns in a variable and print to the terminal

# 5. Call the customer’s shopping cart’s empty cart method

# 6. Check if all products have been removed from the shopping cart



my_customer = Customer('Muto Jenkins')
         
eggs = Product('eggs', 'dairy', 8.00)
milk = Product('milk', 'dairy', 7.00)
# donuts = product('dozen donuts', 7, 'bakery')
# white_loaf_bread = product('white loaf bread', 5, 'bakery')
# wheat_loaf_bread = product('wheat loaf bread', 6, 'bakery')
red_apples = Product('red apples', 'produce', 7.00)
# carrots = product('carrots', 4, 'produce')         
# potatoes = product('potaoes', 10, 'produce')   
# bananas = product('bananas', 5, 'produce')      
# onions = product('onions', 8, 'produce')  
# cornflakes = product('corn flakes', 8, 'breakfast'       
# oatmeal = product('oatmeal', 13, 'breakfast')
# # fruit_smoothy_mix = product('fruity smoothy mix', 12, 'breakfast')
# toilet_paper = product('toilet paper', 21, 'paper products')
# # paper_towels = product('paper towels', 24, 'paper products')
# cheese_pizza = product('cheese pizza', 10, 'frozen foods')
# # supreme_pizza = product('supreme pizza', 13, 'frozen foods')
# chicken_pot_pie = product('chicken pot pie', 15, 'frozen')

# Print name to terminal
print(f'Customer name: {my_customer.name}')

#add products to cart
my_customer.add_item_to_cart(eggs)
my_customer.add_item_to_cart(milk)
my_customer.add_item_to_cart(red_apples)

#get total

total = my_customer.cart.calculate_cart_total()
print(f'The total for {my_customer.name} cart is {total}.')

#empty cart and confirm cart empty
my_customer.cart.empty_cart()
my_customer.view_cart
