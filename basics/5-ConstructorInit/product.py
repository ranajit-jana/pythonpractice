

class Product:
    def __new__(cls):
        print("Creating a new Product instance")
        return super().__new__(cls)

    

p = Product()  # Create an instance of Product

##################################################################
# please explain why super method can take Product and cls as arguments and what is the difference if i dont pass any argumnet

# product.py
# Used 1 reference
# What super(type, obj) means

# The first arg (type) tells Python "start looking for methods after this class in the MRO".
# The second arg (obj) is the object or class to which descriptors are bound (usually an instance like self, or the class like cls).
# Example: super(Product, cls) — search the MRO of cls starting after Product; bind lookups to cls.
# Why super() (no args) works inside methods

# In Python 3 the compiler inserts a hidden class cell for methods defined in the class body. A plain super() uses that class and the method's first parameter (self or cls) automatically, so inside def new(cls): super().new(cls) is equivalent to super(Product, cls).new(cls).
# This is the common, concise form and is preferred when the method remains defined in the class body.
# When omission breaks or differs

# If the function is not a normal method in the class body (moved, assigned elsewhere, or called as a plain function) the implicit class cell is not available and plain super() raises RuntimeError: "super(): class cell not found".
# In @staticmethod there is no self/cls to infer, so plain super() cannot be used.
# Using explicit super(Product, cls) is more verbose but works even if the implicit class cell is not present (and is the only option in older Python versions).
# Concrete short example


# # equivalent inside class body
# return super().__new__(cls)

# # same as
# return super(Product, cls).__new__(cls)

# Summary: both forms do the same inside a normal class method; explicit arguments control MRO start and binding and are required when the implicit context for plain super() is absent.


#################################################################
#  have not added annotation for the new method with @classthod but if i add same annotation i get error - TypeError: Product.new() takes 1 positional argument but 2 were given

# product.py
# Used 1 reference
# Providing code suggestion for __new__
# Short answer: don't use @classmethod on new. new is already called with the class as its first argument by the object creation machinery; decorating it as a classmethod causes the class to be bound twice, producing the TypeError.

# Why that happens (concise):

# When you do Product(), Python effectively calls Product.new(Product, ...). new is expected to be a function that takes cls as its first parameter.
# @classmethod wraps the underlying function in a descriptor that returns a function already bound to the class. The interpreter still calls the attribute with the class argument, so the underlying function receives the class twice (hence "takes 1 positional argument but 2 were given").
# Examples:


# # correct — normal __new__
# class Product:
#     def __new__(cls):
#         print("Creating a new Product instance")
#         return super().__new__(cls)p = Product()  
# # OK

# # wrong — classmethod on __new__ (raises TypeError)
# class Product:    
# @classmethod    
#   def __new__(cls):
#         print("Creating a new Product instance")
#         return super().__new__(cls)p = Product()
#   # TypeError: Product.__new__() takes 1 positional argument but 2 were given
# Alternatives:

# Remove @classmethod on new. Use a normal def new(cls, ...) signature.
# For alternative constructors use @classmethod with a different name (e.g., from_data(cls, ...)) that returns cls(...).
# If you need to customize instance creation at the metaclass level, implement/override the metaclass call or metaclass new.
# If you want, I can patch your product.py to remove the decorator and add a proper init or an alternative constructor.