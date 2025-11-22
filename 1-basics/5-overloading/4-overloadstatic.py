
# add a example of overloading static method in python
class MathOperations:
    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def multiply(a, b, c=1):
        return a * b * c
    
# Usage
result1 = MathOperations.multiply(2, 3)
result2 = MathOperations.multiply(2, 3, 4)
print("Result of multiply(2, 3):", result1)  # Output: Result of multiply(2, 3): 6
print("Result of multiply(2, 3, 4):", result2)  # Output: Result of multiply(2, 3, 4): 24

