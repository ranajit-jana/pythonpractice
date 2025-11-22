
# Default __new__ and __init__ methods
# In Python, if you don't define __new__ or __init__ methods in your class,
# the default implementations from the base class (usually object) are used.


class Product:
    def __new__(cls):
        print("Creating a new Product instance")
        productAddress = super().__new__(cls)
        print(f"Product instance created at address: {id(productAddress)}")
        return productAddress
    
    def __init__(self):
        self.pid = 1
        self.name = "name"
        self.price = 100
        print(f"Initialized Product: {self.pid}, {self.name}, {self.price}")



p = Product()
