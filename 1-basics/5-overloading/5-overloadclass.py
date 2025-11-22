# write a code to overload class method in python

class MathOperations:
    @classmethod
    def multiply(cls,a, b):
        print(" =====inside multiply with 2 parameters========")
        return a * b

    @classmethod
    def multiply(cls, a, b, c=1):
        print(" inside multiply with c=1")
        result = a * b * c
        print(" multiply result:", result)
        return result
    

# Usage
result1 = MathOperations.multiply(2, 3)
result2 = MathOperations.multiply(2, 3, 4)
print("Result of multiply(2, 3):", result1)  # Output:
print("Result of multiply(2, 3, 4):", result2)  # Output:

#     result0 = calc.add(10)
# TypeError: calculate.add() missing 1 required positional argument: 'b'

# why did it gave error when i called multiply with 2 parameters
# In Python, if you define multiple methods with the same name in a class,
# the last definition will overwrite the previous ones. Therefore, when you
# call multiply with 2 parameters, it will result in a TypeError because the
# last defined multiply method expects at least 2 parameters (a and b) and has
# an optional third parameter (c). If you want to support both 2 and 3
# parameters, you should define a single multiply method with a default value
# for c, as shown in the code above.