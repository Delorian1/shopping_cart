# As a developer, I want the ShoppingCart class to have class properties 
# to keep track of the ShoppingCart’s products (list).

# As a developer, I want the ShoppingCart class to have a method to calculate 
# and return the current total of all products in the cart.

# As a developer, I want the ShoppingCart class to have a method to add a new 
# product to the cart. (Appending to the products list)

# As a developer, I want the ShoppingCart class to have a method to empty all
# products from the shopping cart.

class ShoppingCart:

    def __init__(self) -> None:
        self.products = []
 
    def calculate_cart_total(self):
        final_cart_total = 0
        for product in self.products:
           final_cart_total += product.price
        return final_cart_total 

    def add_item_to_cart(self, product):
        self.products.append(product)
        print(f'Your {product.name} were added to cart!')

    def empty_cart(self):
        self.products.clear()
        print("Shopping cart is now empty!")
