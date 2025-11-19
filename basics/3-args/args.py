#varargs
# parameter with variable number of arguments
class Testing:
    #args are passed as tuple
    @classmethod # If i am using classmethod then i have to pass cls as first argument
    def display(cls, *args): # if i pass cls as first argument then it will take class reference 
        # if i dont mark this method as class method cls is considered as normal argument and has not 
        # any special meaning
        print(f"Class reference: {cls}")
        print(type(args))
        print(args)
    #kwargs are passed as dictionary
    @classmethod
    def display_kwargs(cls, **kwargs):
        print(type(kwargs))
        print(kwargs)
    @classmethod
    def display_both(cls, *args, **kwargs):
        print("Args:", args)
        print("Kwargs:", kwargs)

    #@classmethod
    #def display_wrong_order(cls, **kwargs, *args):
        # This will raise a SyntaxError because *args must come before **kwargs
    #    pass
    # args must come before kwargs


Testing.display(1, 2, 3, 4, 5)  # Passing multiple arguments
Testing.display('a', 'b', 'c')  # Passing multiple arguments of different types
Testing.display()  # Passing no arguments 

Testing.display_kwargs(name="Alice", age=30, city="New York")  # Passing multiple keyword arguments
Testing.display_kwargs()  # Passing no keyword arguments

Testing.display_both(1, 2, 3, name="Bob", age=25)  # Passing both args and kwargs
