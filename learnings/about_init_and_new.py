class Employee:
    def __new__(cls, name, id):
        print("Calling __new__ method")
        print("Creating instance of Employee")
        instance = super().__new__(cls)
        return instance

    def __init__(self, name, id):
        print("Calling __init__ method")
        print("Initializing instance of Employee")
        self.name = name
        self.id = id


class ImmutablePoint:
    def __new__(cls, x, y):
        instance = super().__new__(cls)
        super().__setattr__(instance, 'x', x)
        super().__setattr__(instance, 'y', y)
        return instance
    
    def __setattr__(self, key, value):
        raise AttributeError("ImmutablePoint is immutable")
    
    def __init__(self, x, y):
        pass


# Creating an instance of Employee
employee1 = Employee("John Doe", 12345)
point1 = ImmutablePoint(10, 20)
print(point1.x)  # Output: 10
print(point1.y)  # Output: 20
print("Attempting to modify point1's x attribute...")
point1.x = 30  # This will work, but it is not recommended to modify attributes of an immutable class
print(point1.x)  # Output: 30

