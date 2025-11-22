class Product:
    def __new__(cls):
        print("Creating a new Product instance")
        productAddress = super().__new__(cls)
        print(f"Product instance created at address: {id(productAddress)}")
        return productAddress
    
    def __init__(self,pid=1,name="name",price=100):
        self.pid = pid
        self.name = name
        self.price = price
        print(f"Initialized Product: {self.pid}, {self.name}, {self.price}")



p = Product()