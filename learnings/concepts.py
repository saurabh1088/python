# Simple class with no properties
class SampleClassDeclaration:

    def __init__(self):
        print("Initialising class SampleClassDeclaration...")
        pass

class SampleClassWithInstanceProperties:

    def __init__(self, property):
        print("Initialising class SampleClassWithInstanceProperties...")
        self.property = property

    def __str__(self):
        return f"This SampleClassWithInstanceProperties instance property's value is {self.property}\n- Type of property is {type(self.property)}"

class SampleClassWithTypeProperties:

    typeProperty = "value_for_type_property"

    def __init__(self):
        pass

def example_dynamic_typing_in_python():
    x = 10
    print(f"x is {x} and type of x is {type(x)}")
    
    x = 1.5
    print(f"x is {x} and type of x is {type(x)}")

    x = "string"
    print(f"x is {x} and type of x is {type(x)}")

def example_create_object_for_sample_class_with_instance_properties():
    objectOne = SampleClassWithInstanceProperties(property="string")
    objectTwo = SampleClassWithInstanceProperties(property=100)
    print(objectOne)
    print(objectTwo)

def example_create_object_for_sample_class_with_type_properties():
    objectOne = SampleClassWithTypeProperties()
    objectTwo = SampleClassWithTypeProperties()
    objectThree = SampleClassWithTypeProperties()

    print("Initial value for type property across multiple instances")
    print(f"Object 1 : {objectOne.typeProperty}")
    print(f"Object 2 : {objectOne.typeProperty}")
    print(f"Object 3 : {objectOne.typeProperty}")

    print("Updating type property value using objectOne...")
    print("Update finished, printing values again...")
    objectOne.typeProperty = "updated_type_proprty_value"

    print(f"Object 1 : {objectOne.typeProperty}")
    print(f"Object 2 : {objectOne.typeProperty}")
    print(f"Object 3 : {objectOne.typeProperty}")
