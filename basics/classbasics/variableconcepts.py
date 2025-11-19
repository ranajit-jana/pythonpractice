
#implement all three variable concepts: instance variable, class variable, and static variable

class VariableConcepts:
    class_var = "I am a class variable"  # Class variable

    def __init__(self, instance_var):
        self.instance_var = instance_var  # Instance variable

    @staticmethod
    def static_method():
        static_var = "I am a static variable"  # Local variable in static method
        return static_var
    
obj = VariableConcepts("I am an instance variable")
print(VariableConcepts.class_var)          # Accessing class variable
print(obj.instance_var)                     # Accessing instance variable
print(VariableConcepts.static_method())     # Accessing static variable through static method
# mutate static variable
VariableConcepts.class_var = "Class variable changed"
print(VariableConcepts.class_var)          # Accessing mutated class variable

# mutate instance variable
print(f"Address of obj: {id(obj)}")
print(f"Address of instace variable changed",{id(obj.instance_var)} )
obj.instance_var = "Instance variable changed"
print(obj.instance_var)                     # Accessing mutated instance variable
# print the address of the object
print(f"Address of instace variable changed",{id(obj.instance_var)} )
print(f"Address of obj: {id(obj)}")


class Testing:
    class_var = "I am a class variable"
    
    def __init__(self, instance_var):
        self.instance_var = instance_var
        a = 10  # Local variable, not accessible outside this method
obj = Testing("I am an instance variable")
print(Testing.class_var)          # Accessing class variable
print(obj.instance_var)           # Accessing instance variable
# print(a)                        # This would raise an error since 'a' is not accessible here

