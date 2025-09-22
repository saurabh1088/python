class Vehicle:
    class_variable = "I am class variable defined in Vehicle class"
    
    def __init__(self):
        self.instance_variable = "I am instance variable defined in Vehicle class"
        pass
    
    def start_engine(self):
        raise NotImplementedError("Subclasses must implement this method")
    
    def stop_engine(self):
        raise NotImplementedError("Subclasses must implement this method")
        
class Car(Vehicle):
    def __init__(self):
        super().__init__()
        
    def start_engine(self):
        print("Car is started")
        
    def stop_engine(self):
        print("Car is stopped")
        
class Bike(Vehicle):
    def __init__(self):
        super().__init__()
        
    def start_engine(self):
        print("Bike is started")
        
    def stop_engine(self):
        print("Bike is stopped")

def example_vehicle():
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
    car = Car()
    print(car.start_engine())
    print(car.stop_engine())
    
def example_bike():
    bike = Bike()
    print(bike.start_engine())
    print(bike.stop_engine())
    
def class_variables_playground():
    print(f"Vehicle class variable : {Vehicle.class_variable}")
    print(f"Car class variable : {Car.class_variable}")
    print(f"Bike class variable : {Bike.class_variable}")
    Vehicle.class_variable = "I am modified class variable"
    print("After modifying Vehicle.class_variable")
    print(f"Vehicle class variable : {Vehicle.class_variable}")
    print(f"Car class variable : {Car.class_variable}")
    print(f"Bike class variable : {Bike.class_variable}")

def instance_variables_playground():
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
    print(f"Vehicle class variable : {Vehicle.class_variable}")
    vehicle = Vehicle()
    print(f"Vehicle class variable accesses via instace : {vehicle.class_variable}")

def can_instance_update_class_variable():
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


if __name__ == "__main__":
    override_behaviour_for_class_variables_via_subclasses()
