# Simple class with no properties
class SampleClassDeclaration:

    def __init__(self):
        print("Initialising class SampleClassDeclaration...")
        pass

class SampleClassWithProperties:

    def __init__(self, property):
        print("Initialising class SampleClassWithProperties...")
        self.property = property

    def __str__(self):
        return f"This SampleClassWithProperties instance property's value is {self.property}\n- Type of property is {type(self.property)}"

def example_dynamic_typing_in_python():
    x = 10
    print(f"x is {x} and type of x is {type(x)}")
    
    x = 1.5
    print(f"x is {x} and type of x is {type(x)}")

    x = "string"
    print(f"x is {x} and type of x is {type(x)}")

def example_create_object_for_sample_class_with_properties():
    objectOne = SampleClassWithProperties(property="string")
    objectTwo = SampleClassWithProperties(property=100)
    print(objectOne)
    print(objectTwo)
