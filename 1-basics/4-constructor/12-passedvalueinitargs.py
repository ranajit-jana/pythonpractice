class Product:
    def __new__(cls,*args,**kwargs):
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

