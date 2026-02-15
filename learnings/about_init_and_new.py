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

# Creating an instance of Employee
employee1 = Employee("John Doe", 12345)
    