

class Testing:
    class_var = "I am a class variable"

    def __init__(self, instance_var):
        self.instance_var = instance_var
        a = 10  # Local variable, not accessible outside this method



obj = Testing("I am an instance variable")
print(Testing.class_var)          # Accessing class variable
print(obj.instance_var)           # Accessing instance variable
# print(a)                        # This would raise an error since 'a' is not accessible here