

class Test:
    def test(cls):
        print("Test class method called")


Test.test(cls=Test)

# The above code works because we are explicitly passing the class Test as an argument to the test method.
# However, if we were to decorate the test method with @classmethod, it would automatically receive the class as its first argument, and we wouldn't need to pass it explicitly.
# Here's how it would look with @classmethod:
# class Test:
#     @classmethod
#     def test(cls):
#         print("Test class method called")