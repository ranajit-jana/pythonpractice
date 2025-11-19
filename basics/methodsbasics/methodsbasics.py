
# basics of methods in class

#A method is a function that is associated with an object. In Python, methods are defined within a class and are used to perform operations on the data contained within the class. Methods can access and modify the attributes of the class, and they can also take parameters and return values.
class MethodBasics:
    def instance_method(self):
        return "I am an instance method"
    @classmethod
    def class_method(cls):
        return "I am a class method"
    @staticmethod
    def static_method():
        return "I am a static method"
obj = MethodBasics()
print(obj.instance_method())  # Accessing instance method
print(MethodBasics.class_method())  # Accessing class method
print(MethodBasics.static_method())  # Accessing static method 
# Mutating instance method (not common practice, but possible)
print(f"Address of instance_method before mutation: {id(obj.instance_method)}")
def new_instance_method(self):
    return "I am a new instance method"
obj.instance_method = new_instance_method.__get__(obj)  # Bind the new method to
print(obj.instance_method())  # Accessing mutated instance method
print(f"Address of instance_method after mutation: {id(obj.instance_method)}")
# Mutating class method
print(f"Address of class_method before mutation: {id(MethodBasics.class_method)}")
@classmethod
def new_class_method(cls):
    return "I am a new class method"
MethodBasics.class_method = new_class_method
print(MethodBasics.class_method())  # Accessing mutated class methodSS
print(f"Address of class_method after mutation: {id(MethodBasics.class_method)}")
# Mutating static method
print(f"Address of static_method before mutation: {id(MethodBasics.static_method)}")
@staticmethod
def new_static_method():
    return "I am a new static method"
MethodBasics.static_method = new_static_method
print(MethodBasics.static_method())  # Accessing mutated static method
print(f"Address of static_method after mutation: {id(MethodBasics.static_method)}")