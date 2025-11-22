

class calculate:

    def add(self, a):
        print(" print a" , a)
        return a
    def add(self, a, b):
        print(" ------- inside a b -------------" )
        return a + b



    def add(self, a, b, c=0):
        print(" print c'abc'" , c)
        return a + b + c
    


calc = calculate()
# result0 = calc.add(10)
# print("Result of add(10):", result0)  # This will print 10 
#     result0 = calc.add(10)
# TypeError: calculate.add() missing 1 required positional argument: 'b'
result1 = calc.add(10, 20)
result2 = calc.add(10, 20, 30)
print("Result of add(10, 20):", result1)  # This will print 60
print("Result of add(10, 20, 30):", result2)

# explain c=0 in method definition
# In the method definition def add(self, a, b, c=0):, the
# parameter c has a default value of 0. This means that if the caller
# does not provide a value for c when calling the add method, c will
# automatically take the value of 0.
# which method will be called when i call add with 2 parameters
# In Python, if you define multiple methods with the same name in a class,
# the last definition will overwrite the previous ones. Therefore, when you
# call add with 2 parameters, it will result in a TypeError because the
# last defined add method expects at least 2 parameters (a and b) and has
# an optional third parameter (c). If you want to support both 2 and 3
# parameters, you should define a single add method with a default value
# for c, as shown in the code above.