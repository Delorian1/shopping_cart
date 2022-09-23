from shopping_cart import ShoppingCart
# As a developer, I want the Customer class to have class instance 
# variables to keep track of the Customer’s name and shopping cart object. 
#(Set the shopping cart instance variable equal to a new ShoppingCart 
# object in the initializer HINT:
# You will have to import the ShoppingCart class into the customer.py file)

# As a developer, I want the Customer class’s initializer to take in the 
# initial value for the customer’s name via a parameter.

# As a developer, I want the Customer class to have a method to 
# add a new product to the customer’s shopping cart # (within this 
# method you will call the shopping cart’s add product method)

# As a developer, I want the Customer class to have a method to view
#  all products in the customer’s shopping cart.(Loop over the shopping 
# cart’s products list and print each product to the terminal)

class Customer:

    def __init__(self, name) -> None:
        self.name = name
        self.cart = ShoppingCart()

    def add_item_to_cart(self, product):
        self.cart.add_item_to_cart(product)
        print(f'{self.name} added {product.name} to cart!')

    def view_cart(self):
        for product in self.cart.products:
            print(product.name)
