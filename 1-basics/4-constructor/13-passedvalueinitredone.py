class Product:
    def __new__(cls):
        print("Creating a new Product instance")
        productAddress = super().__new__(cls)
        print(f"Product instance created at address: {id(productAddress)}")
        return productAddress
    
    def __init__(self,pid,name,price):
        self.pid = pid
        self.name = name
        self.price = price
        print(f"Initialized Product: {self.pid}, {self.name}, {self.price}")



p = Product(1, "name", 100)

#Error Thrown
# Product instance created at address: 134852476550784
# Traceback (most recent call last):
#   File "/home/rj/pythonpractice/basics/4-constructor/passedvalueinitredone.py", line 16, in <module>
#     p = Product()
# TypeError: Product.__init__() missing 3 required positional arguments: 'pid', 'name', and 'price'