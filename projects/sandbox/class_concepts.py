class Vehicle:
    def __init__(self):
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
    print(vehicle.start_engine())
    
def example_car():
    car = Car()
    print(car.start_engine())
    print(bike.stop_engine())
    
def example_bike():
    bike = Bike()
    print(bike.start_engine())
    print(bike.stop_engine())

if __name__ == "__main__":
    example_vehicle()
    example_car()
    example_bike()
