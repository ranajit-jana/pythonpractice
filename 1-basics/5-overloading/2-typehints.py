

class TypeHinted:
    def greet(self, name: str) -> str:
        return f"Hello, {name}!"

    def add(self, a: int, b: int) -> int:
        return a + b

    def divide(self, numerator: float, denominator: float) -> float:
        if denominator == 0.0:
            raise ValueError("Denominator cannot be zero.")
        return numerator / denominator
    


th = TypeHinted()
greeting = th.greet("Alice")
sum_result = th.add(10, 20)
division_result = th.divide(10.0, 2.0)
print(greeting)  # Output: Hello, Alice
print(f"Sum: {sum_result}")  # Output: Sum: 30

# type hints do not enforce type checking at runtime
# They are mainly for documentation and can be used by static type checkers
# like mypy to catch type-related errors before running the code.
# this is for readability and maintainability of the code.
# this is to help developers understand what types of arguments
# a function expects and what type it will return.
