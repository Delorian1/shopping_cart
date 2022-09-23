# As a developer, I want the Product class to have 
# class properties to keep track of the Product’s name, price, and category.

#X As a developer, I want the Product class’s initializer to take in the 
# initial values for the name, price, and category via parameters


class Product:

    def __init__(self, name, category, price) -> None:
        self.name = name
        self.category = category
        self.price = price

    