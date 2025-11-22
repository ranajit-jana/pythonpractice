class SplinTarget:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"SplinTarget(x={self.x}, y={self.y})"   
    

target1 = SplinTarget(10.5, 20.3)
target2 = SplinTarget(5.0, 15.0)

print(target1)  # Output: SplinTarget(x=10.5, y=20.3)
print(target2)  # Output: SplinTarget(x=5.0, y=15.0)


#  explain slin target 
# The SplinTarget class represents a target point in a 2D space
# is it introduced in python 3.12 



# with x and y coordinates.