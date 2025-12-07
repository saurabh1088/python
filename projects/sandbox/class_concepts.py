import asyncio

class Vehicle:
    """
    Base class representing a generic vehicle.
    
    This class demonstrates abstract methods and class/instance variable concepts.
    It serves as a parent class for specific vehicle types like Car and Bike.
    
    Attributes:
        class_variable (str): A class variable shared by all instances of Vehicle
            and its subclasses. Demonstrates class-level data storage.
    """
    class_variable = "I am class variable defined in Vehicle class"
    
    def __init__(self):
        """
        Initialize a Vehicle instance.
        
        Creates an instance variable that is unique to each Vehicle object.
        This demonstrates the difference between class variables and instance variables.
        """
        self.instance_variable = "I am instance variable defined in Vehicle class"
        pass
    
    def start_engine(self):
        """
        Start the vehicle's engine.
        
        This is an abstract method that must be implemented by subclasses.
        Calling this method on a Vehicle instance will raise NotImplementedError.
        
        Raises:
            NotImplementedError: Always raised, as this is an abstract method
                that must be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses must implement this method")
    
    def stop_engine(self):
        """
        Stop the vehicle's engine.
        
        This is an abstract method that must be implemented by subclasses.
        Calling this method on a Vehicle instance will raise NotImplementedError.
        
        Raises:
            NotImplementedError: Always raised, as this is an abstract method
                that must be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses must implement this method")
        
class Car(Vehicle):
    """
    A concrete implementation of Vehicle representing a car.
    
    This class demonstrates inheritance by extending the Vehicle base class
    and implementing the abstract methods start_engine() and stop_engine().
    """
    def __init__(self):
        """
        Initialize a Car instance.
        
        Calls the parent class constructor to ensure proper initialization
        of inherited attributes.
        """
        super().__init__()
        
    def start_engine(self):
        """
        Start the car's engine.
        
        Implements the abstract method from the Vehicle base class.
        Prints a message indicating that the car has been started.
        """
        print("Car is started")
        
    def stop_engine(self):
        """
        Stop the car's engine.
        
        Implements the abstract method from the Vehicle base class.
        Prints a message indicating that the car has been stopped.
        """
        print("Car is stopped")
        
class Bike(Vehicle):
    """
    A concrete implementation of Vehicle representing a bike.
    
    This class demonstrates inheritance by extending the Vehicle base class
    and implementing the abstract methods start_engine() and stop_engine().
    """
    def __init__(self):
        """
        Initialize a Bike instance.
        
        Calls the parent class constructor to ensure proper initialization
        of inherited attributes.
        """
        super().__init__()
        
    def start_engine(self):
        """
        Start the bike's engine.
        
        Implements the abstract method from the Vehicle base class.
        Prints a message indicating that the bike has been started.
        """
        print("Bike is started")
        
    def stop_engine(self):
        """
        Stop the bike's engine.
        
        Implements the abstract method from the Vehicle base class.
        Prints a message indicating that the bike has been stopped.
        """
        print("Bike is stopped")

def example_vehicle():
    """
    Demonstrate what happens when calling abstract methods on the base class.
    
    Creates a Vehicle instance and attempts to call start_engine(), which
    raises NotImplementedError. This demonstrates that abstract methods
    cannot be called directly on the base class and must be implemented
    by subclasses.
    
    The function catches the exception and prints information about it to
    illustrate the behavior of abstract methods.
    """
    vehicle = Vehicle()
    print("Now this should raise exception")
    try:
        print(vehicle.start_engine())
    except NotImplementedError as e:
        print("Successfully caught the exception!")
        print(f"The exception object is: {e}")
        print(f"The type of the exception is: {type(e)}")
        print("start_engine is called on base class, when it should be called on some concrete implementation by sub-class")
    
def example_car():
    """
    Demonstrate the Car class implementation.
    
    Creates a Car instance and calls both start_engine() and stop_engine()
    methods to show how the abstract methods from the Vehicle base class
    are properly implemented in the Car subclass.
    """
    car = Car()
    print(car.start_engine())
    print(car.stop_engine())
    
def example_bike():
    """
    Demonstrate the Bike class implementation.
    
    Creates a Bike instance and calls both start_engine() and stop_engine()
    methods to show how the abstract methods from the Vehicle base class
    are properly implemented in the Bike subclass.
    """
    bike = Bike()
    print(bike.start_engine())
    print(bike.stop_engine())
    
def class_variables_playground():
    """
    Demonstrate how class variables work across inheritance hierarchy.
    
    Shows that class variables are shared among the class and its subclasses.
    When a class variable is modified on the base class, the change is
    reflected in all subclasses that haven't overridden the variable.
    
    This function prints the class variable values before and after
    modification to illustrate the shared nature of class variables.
    """
    print(f"Vehicle class variable : {Vehicle.class_variable}")
    print(f"Car class variable : {Car.class_variable}")
    print(f"Bike class variable : {Bike.class_variable}")
    Vehicle.class_variable = "I am modified class variable"
    print("After modifying Vehicle.class_variable")
    print(f"Vehicle class variable : {Vehicle.class_variable}")
    print(f"Car class variable : {Car.class_variable}")
    print(f"Bike class variable : {Bike.class_variable}")

def instance_variables_playground():
    """
    Demonstrate how instance variables work independently for each object.
    
    Creates instances of Vehicle, Car, and Bike, and shows that each
    instance has its own copy of instance variables. Modifying an
    instance variable on one object does not affect other instances,
    even if they are of the same class or related through inheritance.
    
    This illustrates the difference between class variables (shared)
    and instance variables (unique per object).
    """
    vehicle = Vehicle()
    car = Car()
    bike = Bike()
    print(f"Vehicle instance variable : {vehicle.instance_variable}")
    print(f"Car instance variable : {car.instance_variable}")
    print(f"Bike instance variable : {bike.instance_variable}")
    vehicle.instance_variable = "I am modified instance variable in vehicle object"
    print("After modifying vehicle.instance_variable")
    print(f"Vehicle instance variable : {vehicle.instance_variable}")
    print(f"Car instance variable : {car.instance_variable}")
    print(f"Bike instance variable : {bike.instance_variable}")

def can_instance_access_class_variable():
    """
    Demonstrate that instances can access class variables.
    
    Shows that an instance of a class can access class variables defined
    in the class. This demonstrates Python's attribute lookup mechanism,
    where instance attributes are checked first, then class attributes.
    """
    print(f"Vehicle class variable : {Vehicle.class_variable}")
    vehicle = Vehicle()
    print(f"Vehicle class variable accesses via instace : {vehicle.class_variable}")

def can_instance_update_class_variable():
    """
    Demonstrate that modifying a class variable via an instance creates an instance variable.
    
    This function illustrates an important Python concept: when you try to modify
    a class variable through an instance, Python doesn't modify the class variable.
    Instead, it creates a new instance variable with the same name, shadowing
    the class variable for that specific instance.
    
    The class variable itself remains unchanged, and other instances continue
    to access the original class variable.
    """
    print(f"Vehicle class variable : {Vehicle.class_variable}")
    vehicle = Vehicle()
    vehicle.class_variable = "I am modified class variable via an instance"
    print("After modifying class variable via instance")
    print(f"Vehicle class variable : {Vehicle.class_variable}")
    print(f"vehicle instance class variable : {vehicle.class_variable}")
    print("This shows that instance cannot modify class variable, it creates a new instance variable with same name")
    print(f"Vehicle.class_variable : {Vehicle.class_variable}")
    print(f"vehicle.class_variable : {vehicle.class_variable}")

def check_if_all_instance_member_get_new_instance_variable_when_class_variable_is_modified_via_instance():
    """
    Verify that modifying class variable via instance only affects that specific instance.
    
    Creates instances of Vehicle, Car, and Bike, then modifies the class variable
    through one instance. This demonstrates that:
    1. The class variable itself remains unchanged
    2. Only the specific instance that performed the modification gets a new
       instance variable
    3. Other instances (even of the same class) continue to access the
       original class variable
    
    This confirms that class variables cannot be modified through instances;
    instead, a new instance variable is created that shadows the class variable.
    """
    print(f"Vehicle class variable : {Vehicle.class_variable}")
    vehicle_instance = Vehicle()
    car_instance = Car()
    bike_instance = Bike()
    print(f"Vehicle instance class variable : {vehicle_instance.class_variable}")
    print(f"Car instance class variable : {car_instance.class_variable}")
    print(f"Bike instance class variable : {bike_instance.class_variable}")
    print("Now modifying class variable via vehicle instance")
    vehicle_instance.class_variable = "I am modified class variable via vehicle instance"
    print("After modifying class variable via vehicle instance")
    print(f"Vehicle class variable : {Vehicle.class_variable}")
    print(f"Vehicle instance class variable : {vehicle_instance.class_variable}")
    print(f"Car instance class variable : {car_instance.class_variable}")
    print(f"Bike instance class variable : {bike_instance.class_variable}")

def override_behaviour_for_class_variables_via_subclasses():
    """
    Demonstrate how subclasses can override class variables.
    
    Shows that subclasses can define their own class variables with the same
    name as the parent class, effectively overriding the inherited class
    variable. When a subclass defines its own class variable, it no longer
    shares the parent's class variable value.
    
    This function:
    1. Shows initial class variable values (all inherited from Vehicle)
    2. Overrides the class variable in Car and Bike subclasses
    3. Shows that each class now has its own independent class variable value
    4. Confirms that the parent Vehicle class variable remains unchanged
    """
    print(f"Present class variable in Vehicle class : {Vehicle.class_variable}")
    print(f"Present class variable in Car class : {Car.class_variable}")
    print(f"Present class variable in Bike class : {Bike.class_variable}")
    print("Now overriding class variable in Car and Bike class")
    Car.class_variable = "I am class variable defined in Car class"
    Bike.class_variable = "I am class variable defined in Bike class"
    print(f"After overriding class variable in Car and Bike class")
    print(f"Present class variable in Vehicle class : {Vehicle.class_variable}")
    print(f"Present class variable in Car class : {Car.class_variable}")
    print(f"Present class variable in Bike class : {Bike.class_variable}")

async def an_async_function_showing_coroutine():
    """
    Demonstrate asynchronous programming with async/await.
    
    This function shows how to create and use async functions (coroutines) in Python.
    It uses asyncio.sleep() to simulate asynchronous work, demonstrating that
    the function can be paused and resumed without blocking the entire program.
    
    The function sleeps for 10 seconds to illustrate the async behavior.
    When called, it returns a coroutine object that must be awaited or run
    using asyncio.run().
    
    Note:
        This function is primarily for demonstration purposes. The 10-second
        sleep is intentionally long to make the async behavior noticeable.
    """
    print("This is an async function")
    print("Simulating some async work with asyncio.sleep")
    print("Sleeping...")
    await asyncio.sleep(10)
    print("Waking up...")
    print("Async function is done")

if __name__ == "__main__":
    asyncio.run(an_async_function_showing_coroutine())
